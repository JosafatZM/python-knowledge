# Escope
# The locations in a program in wich 
# a name can be used. 

# Shadow Variable
# When a local variable shares the same name
# with a global variable.

# global variable
age = 28

def fancy_function():
    
    # Shallow function
    age = 20
    print(age)

# prints the Shallow variable
fancy_function()

# prints the global variable
print(age)

# Espace 1
print()

# CONSTANT
TAX_RATE = 0.06

def calculate_tax(price):
    return price * TAX_RATE

def calculate_tip(price):
    return price * 3 * TAX_RATE

print(calculate_tax(10))
# I'm using round 
print(round(calculate_tip(10), 2))