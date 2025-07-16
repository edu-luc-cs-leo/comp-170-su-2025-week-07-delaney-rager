class Ales:                             #making a super class for ales
    def __init__(self, name: str, abv: float):       #initializing all the common variables between the subclasses
        self.name = name
        self.abv = abv
    def alcohol_content(self, volume_in_oz: float):        #the following two definitions are shared by all of the subclasses
        return self.abv * volume_in_oz  
    def description(self):
        return f"{self.name}: {self.abc*100:.1f}% ABV"  
    
# below is how to make each subclass using the super class by using super
class PaleAle(Ales):
    def __init__(self):
        super().__init__("Pale Ale", 0.055)

class IPA(Ales):
    def __init__(self):
        super().__init__("IPA", 0.065)

class Stout(Ales):
    def __init__(self):
        super().__init__("Stout", 0.07)

class Porter(Ales):
    def __init__(self):
        super().__init__("Porter", 0.06)        
#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 