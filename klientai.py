from main import session,Product,Customer

#customer = Customer(name = "customer 1")
#customer2 = Customer(name = "customer 2")
#customer3 = Customer(name = "customer 3")
customer=session.query(Customer).filter(Customer.id==1).first()
customer2=session.query(Customer).filter(Customer.id==2).first()

product = Product(name = "bananai", price = 3)
product2 = Product(name = "apelsinai", price = 2)
product3 = Product(name = "citrinos", price = 1.5)

#customer.products.append(
#    product3
#)
#customer.products.append(
#   product2
#)
customer2.products.append(
    product3
)
session.commit()
print(customer2.products)
print(customer.products)

#session.add_all([customer,customer2,customer3])
#session.commit()