# both acceot an iterable (such as a list) as an argument and both of these
# functions return a boolean value

# ("all") Returns True if all of the elements in the iterable are truethy or if 
# the iterable is empty
print(all([True]))  # True
print(all([True, True])) # True
print(all([True, True, False])) # False
print(all([1, 2, 3])) # True
print(all([1, 2, 3, 4, 0])) # False
print(all(["a", "b"])) # True
print(all(["a", "b", ""])) # False
print(all([])) # True

print()

# ("any") Returns a True value if any of the elements in the iterable is truethy
print(any([True, False])) #  True
print(any([False, False])) # False
print(any([0, 1])) # True
print(any([0])) # False
print(any([" ", ""])) # True
print(any([""])) # False
print(any([])) # False
