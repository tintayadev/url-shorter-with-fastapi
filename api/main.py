from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from app.schemas import URLCreate, URLResponse
from app.crud import create_short_url, get_url_by_short_id, get_url_by_original_url
from app.database import SessionLocal, engine
from app.models import Base
import os


# Initialize FastAPI app and create tables in the database
app = FastAPI()

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Use the production domain for generating URLs
BASE_URL = os.getenv("BASE_URL", "https://url-shortener-1ssj9dqck-tintayadevs-projects.vercel.app/")


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten/", response_model=URLResponse)
def shorten_url(payload: URLCreate, db: Session = Depends(get_db)):
    # Check if the URL already exists
    db_url = get_url_by_original_url(db, payload.url)
    if db_url:
        return URLResponse(short_url=f"{BASE_URL}/{db_url.short_id}")

    # Create and store the new short URL
    new_url = create_short_url(db, payload.url)
    return URLResponse(short_url=f"{BASE_URL}/{new_url.short_id}")

@app.get("/{short_id}")
def redirect(short_id: str, db: Session = Depends(get_db)):
    db_url = get_url_by_short_id(db, short_id)
    
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return RedirectResponse(url=db_url.original_url)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
