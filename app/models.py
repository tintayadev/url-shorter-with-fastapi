from sqlalchemy import Column, String
from .database import Base

class URL(Base):
    __tablename__ = "urls"

    short_id = Column(String, primary_key=True, index=True)
    original_url = Column(String, unique=True, index=True)
