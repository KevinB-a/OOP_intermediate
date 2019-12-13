from person import *
class Customer(Person):
    """ """
    def __init__(self):
        panier = []
        montant_total = 0
    
    def show_employee_informations(self):
        text=" Employee informations  \n\
        name : {} \n\
        last_name : {} \n\
        age : {} \n\
         : {} \n\ 
        "
        print(text.format(self.name, self.last_name, self.age, self.status))