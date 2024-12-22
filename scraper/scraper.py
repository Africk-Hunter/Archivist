import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re
import aiosqlite
from collections import deque

async def init_db():
    async with aiosqlite.connect('words.db') as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS words
                            (word TEXT PRIMARY KEY, definition TEXT, pronunciation TEXT, word_type TEXT)''')
        await db.commit()

async def save_to_db(word, definition, word_type, pronunciation):
    async with aiosqlite.connect('words.db') as db:
        await db.execute("INSERT OR IGNORE INTO words (word, definition, word_type, pronunciation) VALUES (?, ?, ?, ?)", (word, definition, word_type, pronunciation))
        await db.commit()
        
        async with db.execute("SELECT 1 FROM words WHERE word = ?", (word,)) as cursor:
            entry = await cursor.fetchone()
            if entry:
                print(f"Confirmed entry: {word}")
            else:
                print(f"Entry for word '{word}' not found.")

def is_word_clean(word):
    if " " in word or len(word) < 3 or len(word) > 20 or "-" in word:
        return False
    return True

async def is_in_db(word):
    async with aiosqlite.connect('words.db') as db:
        async with db.execute("SELECT * FROM words WHERE word = ?", (word,)) as cursor:
            entry = await cursor.fetchone()
            if entry:
                return True
            return False
    
def clean_description(description):
    return description.replace("\n", "").strip()
    
def is_word_fully_defined(soup, word_attributes):
    
    found_pronunciation = soup.find('span', class_='word-syllables-entry') 
    found_word_type = soup.find('h2', class_='parts-of-speech') 
    found_defintion = soup.find('div', class_='sense')
    
    if found_pronunciation is None:
        print("Pronunciation not found")
        return False
    if found_word_type is None:
        print("Word Type not found")
        return False
    if found_defintion is None:
        print("Definition not found")
        return False
    
    word_attributes['pronunciation'] = found_pronunciation.text
    word_attributes['word_type'] = found_word_type.text
    word_attributes['definition'] = clean_description(found_defintion.text)

    return True

async def does_word_pass_all_checks(soup, word_attributes):
    word_attributes['word'] = soup.find('h1').text.capitalize()
    word = word_attributes['word']
    
    print(f"Checking word '{word}'")
    
    if not is_word_fully_defined(soup, word_attributes):
        print(f"Word '{word}' is not fully defined. Skipping.")
        return False

    if not is_word_clean(word):
        print(f"Word '{word}' is not clean. Skipping.")
        return False
            
    if await is_in_db(word):
        print(f"Word '{word}' is in database already. Skipping.")
        return False
    return True

def print_word_attributes(word_attributes):
    print(f"Word: {word_attributes['word']}")
    print(f"Definition: {word_attributes['definition']}")
    print(f"Word Type: {word_attributes['word_type']}")
    print(f"Pronunciation: {word_attributes['pronunciation']}")

async def find_word_and_definition(session, url):
    url = clean_url(url)
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            text = await response.text()
            soup = BeautifulSoup(text, 'html.parser')
            
            word_attributes = {'word': '', 'definition': '', 'word_type': '', 'pronunciation': ''}
            
            if await does_word_pass_all_checks(soup, word_attributes):
                print_word_attributes(word_attributes)
                await save_to_db(word_attributes['word'], word_attributes['definition'], word_attributes['word_type'], word_attributes['pronunciation'])
                
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
            url_to_scrape = url_queue.popleft()
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
    url_queue = deque(["https://www.merriam-webster.com/browse/dictionary"])
    visited_urls = set()

    asyncio.run(process_queue(url_queue, visited_urls))
