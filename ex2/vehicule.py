class Vehicule():
    """creation of the vehicle class which has two attributes.
    this class has one method class who check if the vehicule_registration has a good format """

    def __init__(self,vehicule_registration, color):
        """we add two arguments vehicule_registration and color"""
        self.vehicle_registration = vehicle_registration
        self.color = color

    @classmethod
    def check_vehicle_registration(cls,vehicule_registration):
        """this method check if vehicule_registration has a good format """
        cls.expression="123456"
        cls.vehicle_registration = vehicule_registration
        if len(cls.expression) == len(cls.vehicle_registration) and cls.expression.isalnum() and cls.vehicule_registration.isalnum() :
            return cls.vehicule_registration
        else : 
            print("the value is not a good format")
 
        