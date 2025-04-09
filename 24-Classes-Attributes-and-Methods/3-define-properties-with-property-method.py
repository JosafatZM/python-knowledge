# A property has the appearance of an attribute on an object. 
# However, behind the scenes, it invokes an instance method 
# (called a reader) whenever it is accessed and also invokes an 
# instance method (called a writer) whenever a new value is assigned to it.


# Getters & Setters
# Intance methods that get/set attribute values
# on an object 

class Height():
    def __init__(self, feet):
        self._inches = feet * 12

    # The getter method is called when you access the value of the property.
    def _get_feet(self):
        return self._inches / 12
    
    # The setter method is called when you set the value of the property.
    def _set_feet(self, feet):
        if feet >= 0:
            self._inches = feet * 12

    feet = property(_get_feet, _set_feet)


h = Height(5) # calls the setter method
print(h.feet) # calls the getter method

h._set_feet(6) # calls the setter method
print(h._get_feet()) # calls the getter method

h.feet = 4 # calls the setter method
print(h.feet) # calls the getter method