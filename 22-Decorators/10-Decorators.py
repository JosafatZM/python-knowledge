# Decorators 
def uppercase_decorator(function):

    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())

# Applying Multiple Decorators to a Single Function

def split_string(function):

    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string
@uppercase_decorator
def my_name():
    return 'Josafat Zamora'

print(my_name())

# Space
print()
# Accepting Arguments in Decorator Functions

def decorator_with_arguments(function):

    def wrapper_accepting_arguments(arg1, arg2):
        print(f"My arguments are: {arg1} & {arg2}")
        function(arg1, arg2)

    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print(f"Cities I love are {city_one} and {city_two}")

cities("Nairobi", "Accra")

# Space
print()
# Defining General Purpose Decorators

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()

# Space
print()

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1,2,3)

# Space
print()

@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")

function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")

# Space
print()
# Passing Arguments to the Decorator works 

def multiply(factor):
    def decorator(func):
        # In Python, *args and **kwargs are special syntax 
        # that allow you to pass a variable number of arguments
        # to a function.
        # The *args syntax is used to pass a variable number of 
        # non-keyword arguments to a function. These arguments are
        # collected into a tuple.
        # The **kwargs syntax is used to pass a variable number of
        # keyword arguments to a function. These arguments are collected 
        # into a dictionary.
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * factor
        return wrapper
    return decorator

@multiply(2)
def add(a, b):
    return a + b

print(add(a=5, b=5))

# In the context of a decorator, *args and **kwargs are used to pass the original function's
# arguments to the wrapper function, so that the wrapper can call the original function with 
# the same arguments. This allows the decorator to modify the behavior of the original function 
# without knowing anything about its arguments.