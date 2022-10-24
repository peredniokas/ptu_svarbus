from sqlalchemy import column, String, Integer, Date

from base import Base

class Actor(Base):
    __tablename__ = 'actors'
    id = column(Integer, primary_key=True)
    birthday = column(Date)

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday