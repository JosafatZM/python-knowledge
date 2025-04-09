# Higuer Order Function 
# a function that either accepts a function as an argument or returns a function 
# as a return value 

def one():
    return 1

print(type(one))

# First space
print()

# Definig functions
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

# Defining the HOF - Higher Order Function 
def calculate(func, a, b):
    return func(a, b)

# printing the higuer order function (HOF)
print(calculate(add, 5, 6))
print(calculate(substract, 10, 11))

# Second Space
print()

# Josafat's idea of a HOF
def add_ten(func, a, b): 

    # Adding 10 to our normal function result
    total = func(a, b) + 10
    return total 

# Printing Josafat's HOF
print(add_ten(add, 10, 10))


# Define an invoke_thrice function.
# it should accept a sigle argument (wich will be a fucntion)
# In it's body, the invoke_thrice should invoke
# the fucntion that's passed in exactly three times
print("\n-----Ejercicio-----\n")

def invoke_thrice(func):
    func()
    func()
    

def function():
    print("CA")
    print("CA")

invoke_thrice(function)

# Las Space
print()

print(invoke_thrice(function))
# print(invoke_thrice(function)) --> if I do this at the 
#                                    end i will get a 'none'
#                                    Why?, idk!

print()


def multiply(a, b):

  return a * b



def divide(a, b):

  return a / b



def calculate(func, a, b):
    return func(a, b)



print(calculate(multiply, 10, 5))





















