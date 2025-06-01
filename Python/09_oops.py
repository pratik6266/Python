class Car:
  def __init__(self, brand, model): # similar self = this in other language
    self.__brand = brand # doube underscore before any paremeter makes it private
    self.__model = model
    pass

  def get_brand(self): # this is encapsulation making things private and only accessible through getter or setters
    return self.__brand

  def fullname(self):
    print(f"The {self.__brand} model is {self.__model}")

  def fuel_type(self):
    print("Refuling")

  @staticmethod
  def general():
    print("Static method") # are accessible through class not object

  

class Electric_car(Car):
  def __init__(self, battery, brand, model):
    super().__init__(brand, model)
    self.battery = battery
    pass

  def details(self):
    print(self.battery, self.__model, self.__brand)

  def fuel_type(self):
    print("Charging")

# my = Car("Pagani", "Zonda")
# my.fullname()

my = Electric_car("Tesla", "S Plain", "360V")
# my.details()
my.fuel_type()  # This is polymorphism through method overide and overloading by chaning no. of paremeters
Car.general()

print(isinstance(my, Car)) # check and return boolean