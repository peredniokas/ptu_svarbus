from datetime import date
from sqlalchemy import Column, String, Integer, Date

from base import Base

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(date)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date