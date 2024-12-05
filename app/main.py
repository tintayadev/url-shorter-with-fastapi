from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from uuid import uuid4

app = FastAPI()

# In-memory database
db = {}

class URL(BaseModel):
    url: HttpUrl

@app.post("/shorten/")
def shorten_url(payload: URL):
    short_id = uuid4().hex[:6]  # Generate a short ID
    if short_id in db:
        raise HTTPException(status_code=400, detail="Collision occurred")
    db[short_id] = payload.url
    return {"short_url": f"http://localhost:8000/{short_id}"}

@app.get("/{short_id}")
def redirect(short_id: str):
    url = db.get(short_id)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"redirect_to": url}  # Replace with an actual redirect logic
