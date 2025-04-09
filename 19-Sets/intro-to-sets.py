# Set: 
# Is a mutable, data structure that prohibits duplicate values 

stocks = {"MSFT", "TSL", "RIVN", "INV", "IBM", "RIVN"}
print(stocks)
print(len(stocks))

# Espacio 1
print()

lottery_numbers = { (1, 2, 3), (4, 5, 6), (4, 5, 6, 7), (1, 2, 3)}
print(lottery_numbers)

# TypeError 'set' object is not subscriptable 
# means does not aceppt index cause' is not in order
# index = lottery_numbers[0]
# print(index)

# Espacio 2
print()

print("MSFT" in stocks)
print("MSFT" not in stocks)

# Espacio 3
print()

# means they can be iterable
for numbers in lottery_numbers:
    for number in numbers:
        print(number)

# Espacio 4
print()

# Set comprenhension 
# Deletes cause' the squares of the negative numbers are the same as
# the ones for the positive numbers
squares = { number ** 2 for number in [-2, -3, -4, 2, 3, 4]}
print(squares)

# Set comprenhension othe example 
# Does not delete something because cubes of negative numbers are
# different from the ones in positive numbers
cubes = { number ** 3 for number in [-2, -3, -4, 2, 3, 4]}
print(cubes)