from sqlalchemy.orm import Session
from .models import URL
from uuid import uuid4


def create_short_url(db: Session, original_url: str):
    short_id = uuid4().hex[:6]
    db_url = URL(short_id=short_id, original_url=original_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url_by_short_id(db: Session, short_id: str):
    return db.query(URL).filter(URL.short_id == short_id).first()

def get_url_by_original_url(db: Session, original_url: str):
    return db.query(URL).filter(URL.original_url == original_url).first()