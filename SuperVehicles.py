class Vehicle:                              #making a 'super' class of all the vehicles
    def __init__(self, name: str, mpg: int):          #initializing the attributes using self
        self.name = name                    #each vehicles has a name that indicates its type (car/truck/etc.)
        self.mpg = mpg                      #each vehicles also has a specific mpg
    def fuel_needed(self, distance: int):
        return distance / self.mpg          #same function used in the vehicles class
    def description(self):                  #also the same function used in the vehicles class
        return f"{self.name} gets {self.mpg} miles per gallon."
    
#Calling the class for different kinds of vehicles below using the values from
#the Vehicle.py file

class Car(Vehicle):     #in the class vehicle, we are making a subclass car
    def __init__(self):
        super().__init__("Car",30)      #this super references the super class Vehicles and put the input into the __init__ function in the super class

class Truck(Vehicle):
    def __init__(self):
        super().__init__("Truck", 15)

class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__("Motorcycle",50)

class Bus(Vehicle):
    def __init__(self):
        super().__init__("Bus", 8)        
#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 