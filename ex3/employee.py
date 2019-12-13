from person import *

class Employee(Person):
    """ """
    def __init__(self):
        Person.__init__(self)
        self.status = ["employé","technicien", "manager", "cadre"]

    
    def show_employee_informations(self):
        text=" Employee informations  \n\
        name : {} \n\
        last_name : {} \n\
        age : {} \n\
        status : {} \n\ 
        "
        print(text.format(self.name, self.last_name, self.age, self.status))

    @classmethod
    def check_status(cls, employee_status):
        if employee_status in self.status :
            return employee_status
        print("the status of the employee is not referenced")
                