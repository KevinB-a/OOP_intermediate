"""__number_doors pour une variable private ,_number_doors pour une variable protected """
class Clio () :
    colors = {"noir" : 123456,
              "bleu" : 132456,
              "rouge" : 134256,
              "vert" : 134526,
              "blanc" : 134562
              }
    doors = (3, 5)
    price_range = [ 8000, 30000]
    price = 12000
   
    def __init__(self, number_doors, color_number, color):
        self.__number_doors = number_doors
        self.__color_number = color_number
        self.__color = color
    
    @classmethod
    def check_price(cls):
        if self.price_range[0]<= cls.price <= self.price_range[1]:
            return cls.price
        raise ValueError("the value is not in range")

    @property
    def number_doors(self):
        return self.__number_doors
    
    @number_doors.setter
    def number_doors(self, number_doors):
        if number_doors in Clio.doors :
            self.__number_doors = number_doors
        raise ValueError("this value is not allowed ")
    
    @property
    def color_number(self):
        return self.__color_number
    
    @color_number.setter
    def color_number(self, color_number):
        if color_number in Clio.colors.value() :
            self.__color_number = color_number
        raise ValueErrors("this value is not allowed ")
    
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self):
        if color in Clio.colors.keys() :
            self.__color = color
        raise ValueError("this value is not allowed ")


    