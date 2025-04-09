import collections

# easy way to initialize a class
Book = collections.namedtuple("Book", ["title", "author"])
# alternative syntax
# Book = collections.namedtuple("Book", "title author")

animal_farm = Book("Animal Farm", "George Orwell")
gatsby = Book(title = "The Great Gatsby", author = "F. Scott Fitzgerald")

# we can access through index
print(animal_farm[0])
print(animal_farm[-1])
print(animal_farm.title)
print(gatsby.author)
print(type(animal_farm))

class Persona():

    def __init__(self, body) -> None:
        self.body = body

Josa = Persona(1)

print(type(Josa))

print("\n ----- ejercio ----- \n")

# Use the namedtuple function to create a GymExercise class whose instances
# will have three attributes: name, weight, and reps.

# Assign a squat variable to a GymExercise tuple object with 
# a name of “squat”, a weight of 265, and a rep count of 3.

# Assign a bench variable to a GymExercise tuple object with 
# a name of “benchpress”, a weight of 185, and a rep count of 5.

# Assign a deadlift variable to a GymExercise tuple object with
# a name of “deadlift”, a weight of 225, and a rep count of 6.

# Assign a press variable to a GymExercise tuple object with 
# a name of “press”, a weight of 120, and a rep count of 8.

GymExercise = collections.namedtuple("GymExercises", ["name", "weight", "reps"])

squat = GymExercise("squat", 265, 3)
bench = GymExercise("benchpress", 185, 5)
deadlift = GymExercise("deadlift", 225, 6)
press = GymExercise("press", 120, 8)