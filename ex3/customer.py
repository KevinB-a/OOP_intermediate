from product import Product

from person import *
class Customer(Person):
    """this class inherit from Person  """
    def __init__(self, name, last_name, age):
        basket = []
        total_amount = 0
        super().__init__(name, last_name, age)
        product = Product() 
    
    
    def __repr__(self):
        text=" customer informations  \n\
        name : {} \n\
        last_name : {} \n\
        age : {} \n\
        basket : {} \n\
        total_amount : {} \n\ "
        print(text.format(self.name, self.last_name, self.age, self.basket, self.total_amount)) 

    def add_products(self):
        for product in self.products.keys() :
            self.basket.append(product)
    
    #def show_total_amount(self):

