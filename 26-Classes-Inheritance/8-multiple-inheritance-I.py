class FrozenFood():
    def thaw(self, minutes):
        print(f"Thawing for {minutes} minutes")

    def store(self):
        print("Putting in the frezeer!")

class Dessert():
    def add_weight(self):
        print("Putting on the pounds!")

    def store(self):
        print("Putting in the refrigerator!")

class IceCream(FrozenFood, Dessert):
    def store(self):
        print("This is coming from the IceCream class!")

ic = IceCream()

ic.thaw(5)
ic.add_weight()
# runs the first that was inhered
ic.store()

# Method Resolution Order
print(IceCream.mro())
# to look the order classes are going to be invoked 