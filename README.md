# WordMe

## Project Structure

- `backend/`: Contains the Flask backend.
- `frontend/`: Contains the Vue.js frontend.
- `scraper/`: Contains the web scraping script.

## Setup

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

## Running the Project Locally

1. Start the backend server by following the steps in the Backend setup section.
2. Start the frontend server by following the steps in the Frontend setup section.
3. Optionally, run the scraper by following the steps in the Scraper setup section.

The frontend server will be available at `http://localhost:8080` and it will proxy API requests to the backend server running at `http://localhost:5000`.