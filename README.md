# URL Shortener

A simple URL shortener built with FastAPI. This project includes:
- Backend: FastAPI
- Frontend: HTML, CSS
- Deployment: Railway

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd url_shortener
Set up a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install fastapi uvicorn
Run the server:

bash
Copy code
uvicorn app.main:app --reload
Open http://127.0.0.1:8000/ in your browser.