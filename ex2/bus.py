from vehicule import Vehicule

class Bus(Vehicule):
    """class Bus inherit from Vehicule """
    floor = [0,1,2]
    def __init__(self):
        Vehicule.__init__(self)
        self.number_floor = number_floor
    
    @classmethod # we define this method as a class method
    def check_floor(cls): # cls replace self when method is define as a class method
        """metode to check if the number of floors is correct  """
        if self.bus_floor[0] <= cls.number_floor <= self.bus_floor[2]:
            return cls.number_floor
        raise ValueError("the value is not in range")
    
    @property # the get method
    def number_floor(self):
        return self.number_floor
    
    @number_floor.setter #the setter method
    def number_floor(self, number_floor):
        if number_floor in Bus.floor :
            self.number_floors = number_floors
        raise ValueError("this value is not allowed ")