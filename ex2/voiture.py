from vehicule import Vehicule

class Voiture(Vehicule):
    """"""
    doors = [3,4,5]
    def __init__(self):
        Vehicule.__init__(self)
        self.number_doors = number_doors
    
    @classmethod
    def check_doors(cls):
        if self.doors[0] <= cls.number_doors <= self.doors[2]:
            return cls.number_doors
        raise ValueError("the value is not in range")
    
    @property
    def number_doors(self):
        return self.number_doors
    
    @number_doors.setter
    def number_doors(self, number_doors):
        if number_doors in Vehicule.doors :
            self.number_doors = number_doors
        raise ValueError("this value is not allowed ")