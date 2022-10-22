import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask


engine = create_engine('sqlite:///data/filmai.db')
Base = declarative_base()


class Filmas(Base):
    __tablename__ = "filmai"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    director = Column(String(80))
    release_date = Column(DateTime)
    actors = Column(String(255))

    def release_year(self):
            return self.release_date.strftime("%Y")

    def actors_list(self):
            return self.actors.split(',')

class Director(Base):
    __tablename__ = "dirctors"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))

class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))

class Guildmembership(Base):
    __tablename__ = "member"
    id = Column(Integer,primary_key=True)
    guild = Column(String(255))


if __name__ == "__main__":
    Base.metadata.create_all(engine)