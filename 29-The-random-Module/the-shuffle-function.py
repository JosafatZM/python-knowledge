import random 

characters = ["Warrior", "Druid", "Hunter", "Rogue", "Mage"]

# ways of creating a list clone 
clone = characters[:]
clone = characters.copy()

random.shuffle(clone)

print(characters)
print(clone)