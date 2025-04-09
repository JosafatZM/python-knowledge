# Is the idea that multiple objects can 
# react to the same method invocation 

class Person():

    def __init__(self, name, heigth):
        self.name = name
        self.height = heigth

    # the length of a person is represented by their height
    def __len__(self):
        return self.height
    
values = [
    "Josafat", 
    [4, 5, 6, 7],
    (4, 5, 6, 7, 8, 9),
    {"a": 1, "b": 2},
    Person(name= "Josafat", heigth= 75)
]
# these objects are polymorphic bexause they're able 
# to respond to the same magic metod the "__len__"

for value in values:
    print(len(value))
        