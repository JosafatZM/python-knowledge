class Student():

    def __init__(self, math, history, writing) -> None:
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.math + self.history + self.writing
    
    # dunder eq must alwars return a boolean 
    def __eq__(self, __value: object) -> bool:
        return self.grades == __value.grades
    
    def __gt__(self, __value):
        return self.grades > __value.grades 
    
    def __gt__(self, __value):
        return self.grades <= __value.grades 
    
    def __add__(self, __value):
        return self.grades + __value.grades 
    
    def __sub__(self, __value):
        return self.grades - __value.grades 

roberto = Student(math=100, history=100, writing=100)
raul = Student(math=80, history=90, writing=80)
chritian = Student(math=100, history=80, writing=70)

print() #space

print(roberto.grades + raul.grades)
print(roberto.grades / raul.grades)
print(roberto.grades <= raul.grades)

print("\n ----- ejercico ----- \n")

# Part A: Instantiation

# Define a BusTrip class that is initialized with a destination, 
# a bus company, and a price for the trip. 
# Preserve the arguments as attributes on the object.
# The choice of whether to use protected attributes is up to you.

# Part B: String Representation

# The string representation of a BusTrip object must be a string in the form of:
#    "You paid 24.99 to Greyhound to go to Boston.""
# In this example, “Boston” is the destination, “Greyhound” is the bus company, and 24.99 is the price.
# These are all fed in as arguments when a BusTrip object is initialized.

# Part C: Equality

# Implement equality logic between two different BusTrip objects.
# Two BusTrips object are considered equal if:
#   -- they have the same destination
#   -- their price is within 3 dollars of each other
# HINT: Use Python’s abs function to calculate the absolute value of a number.

class BusTrip():

    def __init__(self, destination, company, price) -> None:
        self.destination = destination
        self.company = company
        self.price = price 

    def __str__(self) -> str:
        return f'You paid {self.price} to {self.company} to go to {self.destination}'
    
    # boolean
    def __eq__(self, __value: object) -> bool: # kinda obvious genius 
        return self.destination == __value.destination and abs(self.price - __value.price) <= 3
            

# Sample Execution
boston1 = BusTrip(destination = "Boston", company = "Greyhound", price = 24.99)
boston2 = BusTrip(destination = "Boston", company = "Megabus", price = 22.99)
boston3 = BusTrip(destination = "Boston", company = "Megabus", price = 49.99)
philly  = BusTrip(destination = "Philadelphia", company = "Peter Pan", price = 12.99)

print(boston1)            # You paid 24.99 to Greyhound to go to Boston.
print(boston1 == philly)  # False - different destinations
print(boston1 == boston2) # True - same destination and insignificant price difference
print(boston1 == boston3) # False - large price difference
