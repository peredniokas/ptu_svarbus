from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///data/filmukai.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()


