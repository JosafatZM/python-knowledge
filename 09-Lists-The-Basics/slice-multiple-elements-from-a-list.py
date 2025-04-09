from traceback import print_tb


print("programming"[3:6]) # We go up to 6 bur we dont include 6

muscles = ["Bicep", "Triceps", "Deltoid", "Sartorius"]

print(muscles[1:3])
print(muscles[1:2])

print(muscles[0:2])
print(muscles[:2])
print(muscles[2:1000])
print(muscles[2:])

print(muscles[-4:-2])
print(muscles[-3:])
print(muscles[:-1])

print(muscles[1:-1])

print()

print(muscles[::2])
print(muscles[::-1])
print(muscles[::-2])


print()
# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the third element to the end of the list.
# If the number is odd, return the list elements from index 0 (inclusive) to 2 (exclusive)
#
# EXAMPLE:
# values = ["a", "b", "c", "d", "e", "f"]
# split_in_two(values, 3)     => ["a", "b"]
# split_in_two(values, 4)     => ["c", "d", "e", "f"]
# split_in_two(values, 1)     => ["a", "b"]
# split_in_two(values, 10)    => ["c", "d", "e", "f"]

def split_in_two(list, number):
    if number % 2 == 0:
        return list[2:]
    elif number % 1 == 0 and number % number == 0:
        return list[0:2]
    else:
        return

print(split_in_two(["a", "b", "c", "d", "e", "f"],3))
print(split_in_two(["a", "b", "c", "d", "e", "f"],4))
print(split_in_two(["a", "b", "c", "d", "e", "f"],1))
print(split_in_two(["a", "b", "c", "d", "e", "f"],10))
print(split_in_two(["a", "b", "c", "d", "e", "f"],25))

print()

lista_nueva = ["a", "b", "c", "d", "e", "f"]

if "a" in lista_nueva:
    print("Si esta Perro!!")

if "g" not in lista_nueva:
    print("\nEn efecto no esta Perro!!")

print()

# Declare a nested_extraction function that accepts a list of lists and an index position
#
# The function should use the index as the basis of finding both the nested list
# and the element from that list with the given index postion 
#
# You can asume the number of lists will always be equal to
# the number of elements within each of them 

def nested_extraction(list, index):
    return list[index][index]

lista_n1 = [[3,4,5],[6,7,8],[9,10,11]]

print(nested_extraction(lista_n1,2))
print(nested_extraction(lista_n1,0))
print(nested_extraction(lista_n1,1))

print()
# Declare a beginning_and_end function that accepts a list of elements
#
# It should return True if the first and last elements in the list 
# are equal an False if they are unequal 
# 
# Assume the list will always have at leas 1 element 

def beginning_and_end(list):
    return bool(list[0] == list[-1])

print(beginning_and_end([1,2,3,4,1]))
print(beginning_and_end([1,2,3,4,5]))
print(beginning_and_end(["a","b","a"]))
print(beginning_and_end(["a"]))

print()
# Declare a long_word_in_collection function that accepts a list and a string
# The function should return True if
# - the word exist in the list and
# - the word has more than 4 characters

def long_word_in_collection(list, string):
    return string in list and len(string) > 4

palabras = ["cat", "dog", "rhino"]

print(long_word_in_collection(palabras,"rhino"))
print(long_word_in_collection(palabras,"cat"))
print(long_word_in_collection(palabras,"dog"))