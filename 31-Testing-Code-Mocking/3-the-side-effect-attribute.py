from unittest.mock import Mock
from random import randint

def generate_number():
    return randint(1, 10)

# side_effect wins over 'return_value'
call_me_maybe = Mock(return_value= 10, side_effect= generate_number)

# another way to set the 'side_effect'
#call_me_maybe.side_effect = generate_number

print(call_me_maybe())
print(call_me_maybe())

three_item_list = Mock()
# this imitates the .pop() method form python lists
three_item_list.pp.side_effect = [3, 2, 1, IndexError("pop from empty lsit")]

print(three_item_list.pp())
print(three_item_list.pp())
print(three_item_list.pp())
# print(three_item_list.pop())

print("\n --- Ejercicio --- \n")

# Let's mock a fake Airport object.
# Create a Mock object and assign it to a variable called 'airport'. 
airport = Mock()
# The airport mock should have a 'gates' attribute set to a list of the strings “A1”, “B2”, and “C3”.
airport.gates = ["A1", "B2", "C3"]
# The airport mock should have a 'departures' attribute set to a dictionary where 
# the keys are strings representing cities and the 
# values are strings representating their departure times.
airport.departures = {"Atlanta": "12:00PM",
                      "Nashville": "04:30PM"
                      }

# The airport mock should have a 'close' attribute that is callable (i.e. an instance method). 
# When invoked, it should return the string “Closing”.
def closing():
    return "Closing"

airport.close.side_effect = closing
# The airport should have an 'open' attribute that is callable (i.e. an instance method). .
# When invoked the first time, it should return “Opening…”. 
# When invoked the second time, it should return “Already open”.

airport.open.side_effect = ["Opening...", "Already open"]

# EXAMPLE
#
# Given an airport Mock...
#
print(airport.gates)      # ["A1", "B2", "C3"]
print(airport.departures) # { "Atlanta": "12:00PM", "Nashville": "04:30PM" }
print(airport.close())    # Closing
print(airport.open())     # Opening...
print(airport.open())     # Already open
