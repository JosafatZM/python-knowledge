# inicio de la funcion 
def calculator(operation):

    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b

    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract
# fin de la funcion 

print(calculator("add")(23, 45))
print(calculator("subtract")(23, 45))

# Espace 
print()

def square(num):
    return num ** 2

def cube(num):
    return num ** 3

def times10(num):
    return num * 10

functions = [square, cube, times10]

for function in functions:
    print(function(6))

print("\n-----Ejercicio-----")
# Define an "outer" function that accepts no arguments
# Inside the body of "outer", define an "inner" function
# The "inner" function should return the value 5.
# From "outer", return the uninvoked "inner" function

def outer():

    def inner():
        return 5

    return inner

print(outer()())