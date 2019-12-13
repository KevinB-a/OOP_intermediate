from person import *

class Employee(Person):
    """ """
    def __init__(self, name, last_name, age):
        self.status = ["employé","technicien", "manager", "cadre"]
        super().__init__(name, last_name, age)
    
    def __repr__(self):
        """method to show  """
        text=" Employee informations  \n\
        name : {} \n\
        last_name : {} \n\
        age : {} \n\
        status : {} \n\ 
        "
        print(text.format(self.name, self.last_name, self.age, self.status))

    def employee_autorization(self):
        if self.status[3]>self.status[2] or self.status[3]>self.status[1] or self.status[3]>self.status[0] :
            return True
        elif self.status[2]>self.status[1] or self.status[2]>self.status[0] :
            return True
        elif self.status[1]>self.status[0]:
            return True
        else : 
            return False
    
