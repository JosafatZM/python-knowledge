# an attribute is a piece of data stored on an object
class Guitar():
    def __init__(self):
        print(f'A new object has been created, the object is {self}')

acoustic = Guitar()
electric = Guitar()

# Space
print()

# this code form is not got for software desing

acoustic.year = 1990
acoustic.wood = "Pino"

electric.nickname = "Pinocho"

# this will leed to an error because the objects doesn't have 
# the same attributes 

# print(electric.wood)
# print(acoustic.nickname)

