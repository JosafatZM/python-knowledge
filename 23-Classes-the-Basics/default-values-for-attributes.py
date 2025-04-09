class Book():

    def __init__(self, author, title, price = 14.99):
        self.author = author
        self.title = title
        self.price = price

animal_farm = Book("Jorge Orwell", "Animal Farm")
gatsby = Book("F. Scott", "The great gatsby", 19.99)

print(animal_farm.price)
print(gatsby.price)

# we can also create an instace of a class by using keyword arguments not
# just possitional arguments.
biblia = Book(author= 'Jesus', price= 0, title= 'bible')
print(biblia.price)


# Space
print('----- Ejercicio -----')

# Declare a Zombie class that accepts health and brains_eaten parameters. 
#
# In the initialization process for a Zombie object, assign the 
# two parameters to two attributes with the same name.

# If the instantiation does not pass a health parameter, 
# it should be assigned a default value of 100.
#
# If the instantiation does not pass a brains_eaten parameter, 
# it should be assigned a default value of 5.

class Zombie():

    def __init__(self,brains_eaten = 5, health = 100):
        # attribute 1
        self.health = health
        # attribute 2
        self.brains_eaten = brains_eaten


# Instantiate a Zombie object with 80 health and 5 brains eaten. 
# Assign it to a “bob” variable.
#
# Instantiate a Zombie object with 120 health and 3 brains eaten.
# Assign it to a “sally” variable.
#
# Instantiate a Zombie object with no custom parameters.
# Assign it to a “benjamin” variable.
#
# Practice instantiating the objects with both positional and keyword arguments.

bob = Zombie(brains_eaten= 5, health= 80)

sally = Zombie(health= 120, brains_eaten= 3)

benjamin = Zombie()

print(bob.health)
print(sally.brains_eaten)
print(benjamin.health)