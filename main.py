import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,engine


BASE_DIR=os.path.dirname(os.path.realpath(__file__))


connetion_str='sqlite:///'+os.path.join(BASE_DIR, 'site.sqlite3')


engine=create_engine(connetion_str)

""" table association:
    product_id: int fk (products.id)
    customer_id: int fk(customers.id)

    class klienastas:       
    id                       
    name
    
    class produktai:
    id
    name
    price
    """
Base=declarative_base()