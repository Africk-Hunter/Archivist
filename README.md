# Archivist

## Description

Archivist is a project that utilizes Vue, Python, and SQL to provide users random words and their 
definitions, and gives them the option to display a random word every few seconds based on various 
timer options. Archivist is comprised of two main parts: The Scraper & The Web App

### 1. The Scraper

Archivist utilizes a web crawler/web scraper built in python to scrape and store words from the Merriam-Webster
website, gathing their definitions, their type (noun, adjective, etc), and the pronunciation and storing them in a SQL database 
`words.db`. The scraper only needs to be run once in order to collect and store all of the data, or to add words
that are new to Merriam-Webster. If you're running this project locally, there will already be a populated `words.db`, so running
the scraper will not be necessary.

### 2. The Application

The actual web application for Archivist is built in Vue and connected to the backend using Flask.

## Technologies Used

- **Frontend**: Vue.js
- **Backend**: Flask, Python
- **Web Scraping**: Python, BeautifulSoup
- **Database**: SQLite

## Running Locally

### 1. Install Dependencies

- Navigate to `Archivist/` root directory & run `pip install -r requirements.txt`
- Navigate to `/frontend/` & run `npm install`

### 2. Running scraper (optional)

- Navigate to `/scraper/` & run `python scraper.py`

### 3. Running web application

- Navigate to `/frontend/` & run `npm run serve`
- The frontend server will be available at `http://localhost:8080`.