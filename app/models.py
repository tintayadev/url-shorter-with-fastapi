from sqlalchemy import Column, Integer, String
from app.database import Base

class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_id = Column(String, unique=True, index=True)
    original_url = Column(String, unique=True, index=True)
