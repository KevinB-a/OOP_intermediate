from person import *

class Employee(Person):
    """ """
    def __init__(self, name, last_name, age):
        self.status = status
        super().__init__(name, last_name, age)
        

    def status_employee(self,status):
        if self.status in ["employe", "technicien", "manager", "cadre"] :
            return self.status
        else :
            print("this status doesn't exist")
    
    def __repr__(self):
        """method to show employee informations """
        text=" Employee informations  \n\
        name : {} \n\
        last_name : {} \n\
        age : {} \n\
        status : {} \n"
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
    
