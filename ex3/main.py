from customer import *

from employee import *

employee = Employee("jean-robert", "dupont", 45 )
employee.status_employee("manager")
product = Product() 
product.products["carrot"] = 1
product.products["lemon"] = 2
product.products["apple"] = 1
product.products["mint"] = 1
print(product.products)
print(employee.__repr__())