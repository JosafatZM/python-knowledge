x = 10

def change_stuff():
    global x
    x = 11

print(x)
change_stuff()
print(x)

print("\n----- Ejercicio -----\n")

# Define a global "a" variable assigned to the value 1

a = 1

# Declare a "modify_a" function that accepts a single argument.
# It should overwrite the value of the a global variable with the argument

def modify_a(argument):
    global a
    a = argument

modify_a(3)

print(a)


