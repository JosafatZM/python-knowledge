class Store :

    def __init__(self) -> None:
        self.owner = "Josafat"

    def exclaim(self):
        return "Lots of stuff to buy, come inside!"
    
class CoffeShop(Store):
    pass

starbucks  = CoffeShop()

print(starbucks.owner)
print(starbucks.exclaim())

print("\n ----- ejercicio ------\n")

# Declare a HardwareStore subclass that inherits from the Store superclass.
# Do not define any attributes and methods on the subclass. 
# Use the pass keyword to avoid a class body in HardwareStore.
# Instantiate a new instance of the HardwareStore class and assign it to a home_depot variable.
# Access the value of the "owner" attribute on your HardwareStore instance.
# Invoke the exclaim instance method on your HardwareStore instance.

    
class HardwareStore(Store):
    pass    

home_depot = HardwareStore()

print(home_depot.owner)
print(home_depot.exclaim()) 