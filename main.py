from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('sqlite:///data/parduotuve.db')
Base = declarative_base()

association_table = Table('customer_product', Base.metadata, 
    Column('customer_id', Integer, ForeignKey("customers.id")),
    Column('product_id', Integer, ForeignKey("products.id")),
)


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    products = relationship("Product", secondary=association_table, 
        back_populates="customers",
    )

    def __repr__(self):
       # return f"({self.id}, {self.name})"
        return f"Customer {self.name}"

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    price = Column(Integer, nullable=True)
    customers = relationship(
        "Customer",
        secondary=association_table,
        back_populates="products",
    )

    def __repr__(self):
        return f"Product {self.name}"

if __name__=="__main__":
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

session=sessionmaker()(bind=engine)

