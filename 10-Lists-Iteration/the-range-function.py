# every object that is iterable can be iterated over with 
# the for loop


# They all work

# for number in range(5):
#     print(number)

# print()
# for number in range(1,11):
#     print(number)

# print()
# for number in range(-1,11):
#     print(number)

# print()
# for number in range(10,101,9):
#     print(number)

print()
# The inclusive starting value, the exclusive ending value and the stride interval.
x = 64

for numbers in range(x, 0, -1): # The third elememt represents the gap between subsequent numbers.
    print(numbers)