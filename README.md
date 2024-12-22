# WordMe

## Description

WordMe is a project that includes a Flask backend, a Vue.js frontend, and a web scraping script. The backend serves API endpoints, the frontend provides a user interface, and the scraper collects word definitions from the Merriam-Webster website.

## Technologies Used

- **Backend**: Flask, Python
- **Frontend**: Vue.js, JavaScript
- **Web Scraping**: Python, BeautifulSoup, Requests
- **API**: RESTful API (Flask)
- **Database**: SQLite (Optional, for storing scraped data)
### Backend

1. Navigate to the `backend/` directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the backend server: `python app.py`

### Frontend

1. Navigate to the `frontend/` directory.
2. Install dependencies: `npm install`
3. Run the frontend server: `npm run serve`

### Scraper

1. Navigate to the `scraper/` directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the scraper: `python scraper.py`

### Running the Project Locally

1. Start the backend server by following the steps in the Backend setup section.
2. Start the frontend server by following the steps in the Frontend setup section.
3. Optionally, run the scraper by following the steps in the Scraper setup section.

The frontend server will be available at `http://localhost:8080` and it will proxy API requests to the backend server running at `http://localhost:5000`.