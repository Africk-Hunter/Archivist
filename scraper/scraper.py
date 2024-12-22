import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re
import aiosqlite

async def init_db():
    async with aiosqlite.connect('words.db') as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS words
                            (word TEXT PRIMARY KEY, definition TEXT)''')
        await db.commit()

async def save_to_db(word, definition):
    async with aiosqlite.connect('words.db') as db:
        await db.execute("INSERT OR IGNORE INTO words (word, definition) VALUES (?, ?)", (word, definition))
        await db.commit()
        
        # Confirm the entry was added
        async with db.execute("SELECT * FROM words WHERE word = ?", (word,)) as cursor:
            entry = await cursor.fetchone()
            if entry:
                print(f"Confirmed entry: {entry}")
            else:
                print(f"Entry for word '{word}' not found.")

def is_word_clean(word):
    if " " in word or len(word) < 3 or len(word) > 20 or "-" in word:
        return False
    return True

async def find_word_and_definition(session, url):
    url = clean_url(url)
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            text = await response.text()
            soup = BeautifulSoup(text, 'html.parser')
            word = soup.find('h1').text.capitalize()
            definition = ""
            found_def = soup.find('div', class_='sense')
            
            if not is_word_clean(word):
                print(f"Word '{word}' is not clean. Skipping.")
                return
            
            if found_def is not None:
                definition = found_def.text
            
            print(f"Word: {word}")
            print(f"Definition: {definition}")
            await save_to_db(word, definition)
    except aiohttp.ClientError as e:
        print(f"Failed to retrieve {url}: {e}")

def clean_url(url):
    if url.startswith("/"):
        return "https://www.merriam-webster.com" + url
    return url

async def find_urls(session, soup, visited_urls):
    url_frontier = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            full_url = clean_url(href)
            if full_url not in visited_urls:
                if re.search(r'/browse/dictionary/', href):
                    url_frontier.append(full_url)
                elif re.search(r'/dictionary/\w+', href):
                    await find_word_and_definition(session, full_url)
                    visited_urls.add(full_url)
    return url_frontier

async def scrape_website_for_urls(session, url, visited_urls):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            text = await response.text()
            soup = BeautifulSoup(text, 'html.parser')
            found_urls = await find_urls(session, soup, visited_urls)
            return found_urls
    except aiohttp.ClientError as e:
        print(f"Failed to retrieve {url}: {e}")
        return []

async def process_queue(url_queue, visited_urls):
    async with aiohttp.ClientSession() as session:
        while url_queue:
            url_to_scrape = url_queue.pop(0)
            url_to_scrape = clean_url(url_to_scrape)
            print(f"Processing URL: {url_to_scrape}")

            if url_to_scrape in visited_urls:
                print(f"Already visited: {url_to_scrape}")
                continue

            visited_urls.add(url_to_scrape)
            scraped_data = await scrape_website_for_urls(session, url_to_scrape, visited_urls)

            for next_url in scraped_data:
                if next_url not in visited_urls:
                    print(f"Adding to queue: {next_url}")
                    url_queue.append(next_url)

if __name__ == "__main__":
    asyncio.run(init_db())
    url_queue = ["https://www.merriam-webster.com/browse/dictionary"]
    visited_urls = set()

    asyncio.run(process_queue(url_queue, visited_urls))
