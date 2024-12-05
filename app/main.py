from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from .schemas import URLCreate, URLResponse
from .crud import create_short_url, get_url_by_original_url, get_url_by_short_id
from .database import SessionLocal, engine
from .models import Base


app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten/", response_model=URLResponse)
def shorten_url(payload: URLCreate, db: Session = Depends(get_db)):
    db_url = get_url_by_original_url(db, payload.url)

    if db_url:
        return URLResponse(short_url=f"http://127.0.0.1:8000/{db_url.short_id}")

    new_url = create_short_url(db, payload.url)
    return URLResponse(short_url=f"http://127.0.0.1:8000/{new_url.short_id}")

@app.get("/{short_id}")
def redirect(short_id: str, db: Session = Depends(get_db)):
    db_url = get_url_by_short_id(db, short_id)
    
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return RedirectResponse(url=db_url.original_url)

@app.get("/")
def read_root():
    return {"message": "Welcome to the URL shortener"}

