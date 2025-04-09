import random
class Player():

    def __init__(self, games_played, victories):
        self.games_played = games_played
        self.victories = victories

    
    @property
    def win_ratio(self):
        return self.victories / self.games_played
    

class HumanPlayer(Player):
    
    def make_move(self):
         print('Let player make the decision!')

class ComputerPlayer(Player):
    
    def make_move(self):
        print('Run advanced algorithm to calculate best move!')

hp = HumanPlayer(games_played=100, victories=78)
cp = ComputerPlayer(games_played=1000, victories=999)

print(hp.win_ratio)
print(cp.win_ratio)

game_players = [hp, cp]
# polymorphism here is that doesn't matter what kind of player
# we have as long as it is capable of making a move, so here is 
# multiple objects being able to respond to the same method call 
starting_player = random.choice(game_players)
starting_player.make_move()

print("\n ---- Ejercicio ---- \n")

# In this exercise, we'll be modelling a routine for proper dental health,
# which includes brushing our teeth, flossing, and using mouthwash.
# The order of these three varies from person to person.

# Declare a DentalHealthItem class. Its initialization should set a "price"
# attribute.

class DentalHealthItem():
    def __init__(self):
        self.price = 200

# Declare a Toothbrush subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Brushing the teeth"

class Toothbrush(DentalHealthItem):
    def use(self):
        return "Brushing the teeth"

# Declare a Floss subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Flossing the teeth"\

class Floss(DentalHealthItem):
    def use(selff):
        return "Flossing the teeth"

# Declare a Mouthwash subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Washing the teeth"

class Mouthwash(DentalHealthItem):
    def use(self):
        return "Washing the teeth"

# Instantiate an instance of a Toothbrush and assign it a "toothbrush" variable.
# Instantiate an instance of a Floss and assign it a "floss" variable.
# Instantiate an instance of a Mouthwash and assign it a "mouthwash" variable.

toothbrush = Toothbrush()
floss = Floss()
mouthwash = Mouthwash()

# Declare a "dental_health_kit" variable. It should be a list that stores the three objects.
 
dental_health_kit = [toothbrush, floss, mouthwash]

# Import the "random" module (see last lesson for reference). 
# Invoke the "shuffle" function from the module, passing in the dental_health_kit list. 
# This will mutate the list, randomizing the order of its elements.
random.shuffle(dental_health_kit)
# Use list comprehension to invoke the "use" method on all three objects in "dental_health_kit".
# Assign the resulting list of strings to an "actions" variable.
actions = [item.use() for item in dental_health_kit]
