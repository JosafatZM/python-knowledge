# Is an anonymous function (a function without a name)
# Helps "built in functions" to do it's job

metals = ["gold", "silver", "platinium", "palladium"]
# filter is just an object you have to 
# convert it into a list to the extract the elements
# in it

# "filter" for booleans
print(list(filter(lambda metal: len(metal) > 5, metals)))
print(list(filter(lambda el: len(el) > 5, metals)))
print(list(filter(lambda element: "p" in element, metals)))
print()
# "map" helps the function do it's job
print(list(map(lambda word: word.count("l"), metals)))
print(list(map(lambda word: word.replace("s", "$"), metals)))



print("\n***** Ejercicio *****\n")
# Declare a right_words function that accepts a list of words and a number.
# Return a new list with the words that have a length equal to the number.
# Do NOT use list comprehension.
#
# EXAMPLES:
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3)     => ['cat', 'dog', 'ace']
# right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5)     => ['heart']
# right_words([], 4)                                         => []


def right_words(list_of_words, number):
    return list(filter(lambda animal: len(animal) == number, list_of_words))

print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))
print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 5))
print(right_words([], 4))
# Usando List Comprehension.

animals = ['cat', 'dog', 'bean', 'ace', 'heart']
number = 3
print([animal for animal in animals if len(animal) == number])


print("\n***** Ejercicio *****\n")
# Declare an only_odds function.
# It should accept a list of whole numbers.
# It should return a list with only the odd numbers from the original list.
# Do NOT use list comprehension.
#
# EXAMPLES:
# only_odds([1, 3, 5, 6, 7, 8])      =>  [1, 3, 5, 7]
# only_odds([2, 4, 6, 8])            =>  []

def only_odds(list_of_numbers):
    
    return list(filter(lambda number: number % 2 != 0, list_of_numbers))

print(only_odds([1, 3, 5, 6, 7, 8]))
print(only_odds([2, 4, 6, 8]))

# Usando list comprehension.
numbers = [1, 3, 5, 6, 7, 8]
print([number for number in numbers if number % 2 != 0])

print("\n***** Ejercicio *****\n")
# Declare a count_of_a function that accepts a list of strings.
# It should return a list with counts of how many “a” characters appear per string.
# Do NOT use list comprehension.
#
# EXAMPLES:
# count_of_a(["alligator", "aardvark", "albatross"])    => [2, 3, 2]
# count_of_a(["plywood"])                               => [0]
# count_of_a([])                                        => []

def count_of_a(list_strs):
    return list(map(lambda palabra: palabra.count("a"), list_strs))

print(count_of_a(["alligator", "aardvark", "albatross"]))
print(count_of_a(["plywood"]))
print(count_of_a([]))
# Usando list comprehension.
animals = ["alligator", "aardvark", "albatross"]
print([animal.count("a") for animal in animals])