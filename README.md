# URL Shortener

A simple and efficient URL shortener application built with **FastAPI** and **SQLite**. This app allows users to shorten long URLs and access the original URLs by visiting the shortened URL.

## Features

- **URL Shortening**: Shorten any long URL by providing the original URL.
- **URL Validation**: Ensures the input URL is valid before shortening.
- **Frontend UI**: A simple user interface to interact with the API and generate short URLs.
- **Copy to Clipboard**: Once a short URL is generated, users can easily copy it to their clipboard.

## Technologies Used

- **FastAPI**: For building the backend API.
- **SQLite**: A lightweight database to store the URLs.
- **Jinja2**: For rendering the frontend templates.
- **HTML/CSS**: For building the responsive frontend.
- **JavaScript**: For the copy-to-clipboard functionality.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/url-shortener.git
   cd url-shortener
   ```

2. Create a virtual environment:

   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   uvicorn app.main:app --reload
   ```

   This will start the app at `http://127.0.0.1:8000`.

## Usage

1. **Shorten a URL**:

   - Make a `POST` request to `http://127.0.0.1:8000/shorten/` with the following JSON payload:

     ```json
     {
       "url": "https://example.com"
     }
     ```

   - Example `curl` command:
     
     ```bash
     curl -X 'POST' \
       'http://127.0.0.1:8000/shorten/' \
       -H 'accept: application/json' \
       -H 'Content-Type: application/json' \
       -d '{"url": "https://example.com"}'
     ```

   - You will receive a JSON response with the shortened URL:

     ```json
     {
       "short_url": "http://127.0.0.1:8000/<short_id>"
     }
     ```

2. **Access the Original URL**:

   - To visit the original URL, just navigate to the shortened URL in the browser.

   Example: If the short URL is `http://127.0.0.1:8000/abc123`, you will be redirected to the original URL.

## Frontend

- A simple frontend is included where users can shorten URLs through a clean and minimal interface.
- The short URL generated will be displayed along with a button to copy the short URL to the clipboard for easy sharing.

## Development

1. **Running Tests**:

   To run tests, ensure the virtual environment is activated and use `pytest`:

   ```bash
   pytest
   ```

2. **Adding Features**:

   - Fork the repository and create a new branch for your feature.
   - Once your changes are ready, commit and push them.
   - Open a pull request to merge your changes into the main branch.
