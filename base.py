from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///data/filmukai.db')
Base = declarative_base()



if __name__=="__main__":
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

session=sessionmaker()(bind=engine)
