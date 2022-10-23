import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

BASE_DIR=os.path.dirname(os.path.realpath(__file__))


connetion_str='sqlite:///'+os.path.join(BASE_DIR, 'site.sqlite3')


engine=create_engine(connetion_str)

Base=declarative_base()
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

association_table = Table(
    'association',
    Base.metadata,
    Column('customer_id',ForeignKey('customers.id')),
    Column('product_id', ForeignKey('product.id'))
)

class Customer(Base):
    __table__ = 'customers'
    id = Column(Integer(), primary_key = True)
    name = Column(String(), nullable= False)
    products = relationship('Product',secondary=association_table
        back_populates='customers'
    )

    def __repr__(self):
        return f"<Customer {self.name}>"

class Product(Base):
    __table__ = 'products'
    id = Column(Integer(), primary_key = True)
    name= Column(String(), nullable = False)
    price = Column(String(), nullable= False)
    customers = relationship(
        'Customer',
        secondary = association_table,
        back_populates = 'products'
    )
    def __repr__(self):
        return f"<Product {self.name}>"
