from vehicule import Vehicule

class Voiture(Vehicule):
    """the class Voiture inherit from Vehicule 
    this class has one class argument doors , one class method who check if number_doors is
    good , and get and set method  """
    
    doors = [3,4,5]
    
    def __init__(self, number_doors,vehicule_registration, color):
        """we get the arguments of the class vehicle and we add another argument
        number_doors"""
        self.number_doors = number_doors
        super().__init__(vehicule_registration,color)
        
    
    @classmethod
    def check_doors(cls):
        """this method check if number_doors is in doors list"""
        if Voiture.doors[0] <= cls.number_doors <= Voiture.doors[2]:
            return cls.number_doors
        #raise ValueError("the value is not in range")

    @property
    def number_doors(self):
        """the getter method """
        return self.__number_doors
    
    @number_doors.setter
    def number_doors(self, number_doors):
        """the setter method """
        if number_doors in Voiture.doors :
            self.__number_doors = number_doors
       # raise ValueError("this value is not allowed ")
        else :
            self.__number_doors = False