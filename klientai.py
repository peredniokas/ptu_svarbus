from main import session,Product,Customer

customer = Customer(name = "customer 1")
customer2 = Customer(name = "customer 2")
customer3 = Customer(name = "customer 3")

session.add_all([customer,customer2,customer3])
session.commit()