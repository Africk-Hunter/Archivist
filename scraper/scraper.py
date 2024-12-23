import asyncio
from bs4 import BeautifulSoup
import re
import aiosqlite
from collections import deque
import time
import random
import cloudscraper

scraper = cloudscraper.create_scraper()

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
]  
            
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def get_headers():
    return {
        'User-Agent': get_random_user_agent(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Referer': 'https://www.google.com/',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers'
    }
    
def delay():
    time.sleep(random.uniform(5, 12))
    
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
                print(f"{GREEN}Confirmed entry: {word}{RESET}")
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
    if found_pronunciation is None:
        print(f"{RED}Pronunciation not found{RESET}")
        return False
        
    found_word_type = soup.find('h2', class_='parts-of-speech') 
    if found_word_type is None:
        print(f"{RED}Word Type not found{RESET}")
        return False
        
    found_defintion = soup.find('div', class_='sense')
    if found_defintion is None:
        print(f"{RED}Definition not found{RESET}")
        return False
    
    word_attributes['pronunciation'] = found_pronunciation.text
    word_attributes['word_type'] = found_word_type.text
    word_attributes['definition'] = clean_description(found_defintion.text)

    return True

async def does_word_pass_all_checks(soup, word_attributes):
    word_attributes['word'] = soup.find('h1').text.capitalize()
    word = word_attributes['word']

    print(f"{YELLOW}Checking word '{word}'{RESET}")
    
    if not is_word_fully_defined(soup, word_attributes):
        print(f"{RED}Word '{word}' is not fully defined. Skipping.{RESET}")
        return False

    if not is_word_clean(word):
        print(f"{RED}Word '{word}' is not clean. Skipping.{RESET}")
        return False
            
    if await is_in_db(word):
        print(f"{GREEN}Word '{word}' is in database already. Skipping.{RESET}")
        return False
    return True

def print_word_attributes(word_attributes):
    print(f"Word: {word_attributes['word']}")
    print(f"Definition: {word_attributes['definition']}")
    print(f"Word Type: {word_attributes['word_type']}")
    print(f"Pronunciation: {word_attributes['pronunciation']}")

async def find_word_and_definition(url):
    url = clean_url(url)
    try:
        headers = get_headers()

        response = await asyncio.to_thread(scraper.get, url, headers=headers)
        response.raise_for_status()
        text = response.text
        soup = await asyncio.get_event_loop().run_in_executor(None, BeautifulSoup, text, 'html.parser' )
        
        word_attributes = {'word': '', 'definition': '', 'word_type': '', 'pronunciation': ''}
        if await does_word_pass_all_checks(soup, word_attributes):
            word = word_attributes['word']
            pronunciation = word_attributes['pronunciation']
            word_type = word_attributes['word_type']
            definition = word_attributes['definition']
            
            print(f"Word: {word}")
            print(f"Pronunciation: {pronunciation}")
            print(f"Word Type: {word_type}")
            print(f"Definition: {definition}")
            await save_to_db(word, definition, pronunciation, word_type)
    except cloudscraper.exceptions.CloudflareChallengeError as e:
        print(f"Failed to retrieve {url}: {e}")

def clean_url(url):
    if url.startswith("/"):
        return "https://www.merriam-webster.com" + url
    return url

async def find_urls(soup, visited_urls):
    index = 0
    url_frontier = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            full_url = clean_url(href)
            if full_url not in visited_urls:
                if re.search(r'/browse/dictionary/', href):
                    url_frontier.append(full_url)
                elif re.search(r'/dictionary/\w+', href):
                    await find_word_and_definition(full_url)
                    visited_urls.add(full_url)
                    index += 1
                    print(index)
                    if index % 100 == 0:
                        delay()
    return url_frontier
semaphore = asyncio.Semaphore(5)

async def scrape_website_for_urls(url, visited_urls, retries=5):

    for attempt in range(retries):
        headers = get_headers()
        try:
            response = await asyncio.to_thread(scraper.get, url, headers=headers)
            response.raise_for_status()
            text = response.text
            soup = await asyncio.get_event_loop().run_in_executor(None, BeautifulSoup, text, 'html.parser')
            found_urls = await find_urls(soup, visited_urls)
            return found_urls
        except cloudscraper.exceptions.CloudflareChallengeError as e:
            print(f"Failed to retrieve {url}: {e}")
            if attempt < retries - 1:
                backoff_time = 2 ** attempt
                print(f"Retrying {url} in {backoff_time} seconds (attempt {attempt + 1})")
                time.sleep(backoff_time)
            else:
                return []

async def process_queue(url_queue, visited_urls):
    while url_queue:
        tasks = []
        while url_queue and len(tasks) < 5: 
            url_to_scrape = url_queue.popleft()
            url_to_scrape = clean_url(url_to_scrape)
            print(f"Processing URL: {url_to_scrape}")

            if url_to_scrape in visited_urls:
                print(f"Already visited: {url_to_scrape}")
                continue

            visited_urls.add(url_to_scrape)
            tasks.append(scrape_website_for_urls(url_to_scrape, visited_urls))

        results = await asyncio.gather(*tasks)
        for scraped_data in results:
            for next_url in scraped_data:
                if next_url not in visited_urls:
                    print(f"Adding to queue: {next_url}")
                    url_queue.append(next_url)
        delay()

if __name__ == "__main__":
    asyncio.run(init_db())
    url_queue = deque(["https://www.merriam-webster.com/browse/dictionary"])
    visited_urls = set()

    asyncio.run(process_queue(url_queue, visited_urls))
