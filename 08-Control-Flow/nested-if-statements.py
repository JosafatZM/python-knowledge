ingrediente1 = "psta"
ingrediente2 = "albondigs"

if ingrediente1 == "pasta":
    if ingrediente2 == "albondigas":
        print("Te recomiendo hacer pasta con albondigas")
    else:
        print("I recommend making plain pasata")
else:
    print("I have no recommendations! :/")

if ingrediente1 == "pasta" and ingrediente2 == "albondigas":
    print("Te recomiendo hacer pasta con albondigas")
elif ingrediente1 == "pasta":
    print("I recommend making plain pasata")
else:
    print("I have no recommendations! :/")

print()

# Ejercicios
# Define a divisible_by_three_and_four function that accepts a number as its argument
# it should return True  if number is evenly divisible by both 3 and 4 
# it should return False otherwise

def divisible_by_three_and_four(divisor):
    if divisor % 4 == 0 and divisor % 3 == 0:
        return True
    else:
        return False

print(divisible_by_three_and_four(3))
print(divisible_by_three_and_four(12))
print()

# Modo elegante
def tarea(numero):
    return numero % 4 == 0 and numero % 3 == 0

print(tarea(3))
print(tarea(12))

print()

# Declare a string_theory function that accepts a string as an argument 
# It should return True if the string has more the 3 characters 
# and starts whith a capital "S". It should return False otherwise

def string_theory(word):
    if len(word) > 3 and word[0] == "S":
        return True
    else:
        return False
    
def elegante(string):
    return len(string) > 3 and string[0] == "S"

print(elegante("Sara"))
print(elegante("See"))