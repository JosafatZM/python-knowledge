# superclass
class Animal():
    
    def __init__(self, name):
        
        self.name = name

    def eat(self, food):

        return f"{self.name} is enjoying the {food}"

# subclass
class Dog(Animal):

    def __init__(self, name, breed):
        # "super()" makes our code more stable 
        # cause' if I wanna change the attribute 
        # self.name = name, in the superclass
        # i'll just have to change it there
        super().__init__(name)
        self.breed = breed

mimi = Dog("mimi", "Golden Retriever")

print(mimi.name)
print(mimi.eat("caldo de pollo"))
print(mimi.breed)

print("\n ---- Ejercicio ---- \n")

# Declare a Musician class that accepts a name argument in its initialization.
# The initialization should assign a name argument to a name attribute. 
# In addition, each Musician object should have an "albums" attribute 
# that begins as an empty list.
# Define a release_album instance method on a Musician that accepts a title (string). 
# It should append the string to the end of the list held by the
# albums attribute (see examples below).

class Musician():

    def __init__(self, name):
        self.name = name 
        self.albums = []
    
    def release_album(self, title):
        self.albums.append(title)


#
# Declare a Drummer subclass than inherits from the Musician superclass. 
# In addition to a name, a drummer should also have a stamina attribute 
# represented by an integer. 
# The subclass should invoke the Musician superclass’s initialization procedure
# and pass it the drummer’s name.
# It should also set the stamina attribute in its own initialization process.

class Drummer(Musician):

    def __init__(self, name, stamina):
        super().__init__(name)
        self.stamina = stamina


# EXAMPLE:
lars = Drummer(name = "Lars", stamina = 2)
print(lars.name)   # "Lars"
print(lars.stamina) # 2
print(lars.albums) # []

lars.release_album("Ride the Lightning")
print(lars.albums) # ["Ride the Lightning"]

lars.release_album("Master of Puppets")
print(lars.albums)  # ["Ride the Lightning", 'Master of Puppets']