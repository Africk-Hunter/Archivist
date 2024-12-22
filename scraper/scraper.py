import requests
from bs4 import BeautifulSoup
import queue
import re

def find_word_and_definition(url):
    url = clean_url(url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        word = soup.find('h1').text
        definition = ""
        found_def = soup.find('div', class_='sense')
        if found_def is not None:
            definition = found_def.text
        
        print(f"Word: {word}")
        print(f"Definition: {definition}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {url}: {e}")

def clean_url(url):
    if url.startswith("/"):
        return "https://www.merriam-webster.com" + url
    return url


def find_urls(soup):
    url_frontier = queue.Queue()
    for link in soup.find_all('a'):
        href = link.get('href')
        
        # If url is a layer one url (link that has more links), add to queue
        if href and re.search(r'/browse/dictionary/', href):
            url_frontier.put(href)
            continue
        # If url is a layer two url (is a link to a word), scrape word and definition
        if href and re.search(r'/dictionary/\w+', href):
            find_word_and_definition(clean_url(href))
            find_word_and_definition(href)
            continue
    return url_frontier

def scrape_website_for_urls(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        found_urls = find_urls(soup)
        return found_urls
    else:
        print(f"Failed to retrieve {url}")
        return None

def clean_url(url):
    if url.startswith("/"):
        return "https://www.merriam-webster.com" + url
    return url

def process_queue(url_queue, visited_urls):
    while not url_queue.empty():
        url_to_scrape = url_queue.get()
        url_to_scrape = clean_url(url_to_scrape)
        print(f"Processing URL: {url_to_scrape}")

        if url_to_scrape in visited_urls:
            print(f"Already visited: {url_to_scrape}")
            continue

        scraped = scrape_website_for_urls(url_to_scrape)
        visited_urls.add(url_to_scrape)

        if scraped:
            while not scraped.empty():
                next_url = scraped.get()
                next_url = clean_url(next_url)
                if next_url not in visited_urls:
                    print(f"Adding to queue: {next_url}")
                    url_queue.put(next_url)

if __name__ == "__main__":
    url_queue = queue.Queue()
    visited_urls = set()
    url_queue.put("https://www.merriam-webster.com/browse/dictionary")

    process_queue(url_queue, visited_urls)
