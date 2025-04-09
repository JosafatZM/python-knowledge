# Python is going to intentionally twist your method names 
# and attributte names around to effectively prevent them for
# being used by subclasses 

class Nonesense():
    def __init__(self):
        # an attribute will be mangled if it begins whith dundar (__)
        self.__some_attribute = "Hello"

    def __some_method(self):
        print("This is coming from some_method!")


class SpecialNonesense(Nonesense):
    pass

n = Nonesense()
sn = SpecialNonesense()

# this is the way to access
print(n._Nonesense__some_attribute)
sn._Nonesense__some_method()

# this wonr work
# print(n.__some_attribute)
# n.__some_method()