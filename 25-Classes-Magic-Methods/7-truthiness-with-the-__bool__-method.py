class Emotion():

    def __init__(self, positivity, negativity) -> None:
        self.positivy = positivity
        self.negativity = negativity

    def __bool__(self):
        return self.positivy > self.negativity
    
my_emotional_state = Emotion(positivity= 50, negativity= 75)

if my_emotional_state:
    print("this will not print because I have more negativity than positivity")

my_emotional_state.positivy = 100

if my_emotional_state:
    print("this will print because I have more positivity than negativity")


print() #space

class Person():

    def __init__(self, health: str) -> None:
        self.health = health

class Dog():

    def __init__(self, health: str) -> None:
        self.health = health

P1 = Person("good")
D1 = Dog("bad")

print(P1.health == D1.health)