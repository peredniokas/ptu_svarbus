import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,engine


BASE_DIR=os.path.dirname(os.path.realpath(__file__))


connetion_str='sqlite:///'+os.path.join(BASE_DIR, 'site.sqlite3')


engine=create_engine(connetion_str)


Base=declarative_base()