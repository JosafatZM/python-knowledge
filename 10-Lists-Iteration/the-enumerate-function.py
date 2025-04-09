
errands = ["Go to gym", "Grab lunch", "Get promoted at work", "Sleep"]

print(enumerate(errands))

for index, errand in enumerate(errands, 1):
    print(f"{errand} is number {index} on my to do list for today!")

print()
# Define an in_list function that accepts a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1.
# Do NOT use the find or index methods.
#
# EXAMPLES
strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1

# We use ENUMERATE because can iterate not just over the list elements, but
# but also over the index positions that correspond to each of those elements

def in_list(list, string):
    for index,word in enumerate(list):
        if string == word:
            return index
    return -1

print(in_list(strings, "enchanted"))
print(in_list(strings, "sparks fly"))
print(in_list(strings, "fifteen"))
print(in_list(strings, "love story"))
print(in_list(strings, "long live"))

print()
# Define a sum_of_values_and_indices function that accepts a list of numbers. 
# It should return the sum of all of the elements along with their index values.
#
# EXAMPLES
# sum_of_values_and_indices([1, 2, 3])    => (1 + 0) + (2 + 1) + (3 + 2) => 9
# sum_of_values_and_indices([0, 0, 0, 0]) => 6
# sum_of_values_and_indices([])           => 0

def sum_of_values_and_indices(list):
    total = 0
    for index, number in enumerate(list):
        total = total + index + number
    return total

print(sum_of_values_and_indices([1, 2, 3]))
print(sum_of_values_and_indices([0, 0, 0, 0]))
print(sum_of_values_and_indices([]))

print("\"n ----- Ejercicio Renovado ------\n")
# Define an in_list function that accepts a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1.
# Do NOT use the find or index methods.
#
# EXAMPLES
strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1



