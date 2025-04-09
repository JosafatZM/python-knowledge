# Invokes a function on every element in an iterable 
# 
# Functions are first class objects in python 
# Means that it can be treated as any other data type
# 
# map(function, interval)
# 
# What map is going to do is invoke the function, the very firts argument
# on every element within the second argument (the iterable) 

numbers = [4, 8, 15, 23, 42]
cubes = [number ** 3 for number in numbers]
print(cubes)

print()
def cube(number):
    return number ** 3

print(list(map(cube, numbers)))

animals = ["cat", "bear", "zebra", "donkey", "cheetah"]
length_of_strings = [len(animal) for animal in animals]
# print(length_of_strings)

def length_of_animals(animal):
    return len(animal)

print(list(map(length_of_animals, animals)))

# for animal in map(length_of_animals, animals):
#     print((animal))