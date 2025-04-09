college_courses = {
    "Calculo": "Norma Elva",
    "Biomecanica": "Laura",
    "Anatomia": "Carmen",
    "Embebidos": "Rene"
}
# Otra manera de escribir es:
# for course, professor in college_courses.items():
for key, value in college_courses.items():
    print(f"The key is {key} and the value is {value}")

for _, professor in college_courses.items():
    print(f"{professor} ha sido de mis profes favoritos")

print()
print("----- Ejercicio ---- \n")
# Declare an invert function that accepts a dictionary object. 
# The function should return a new dictionary where the keys and values from the original dictionary are inverted. 
# Each key should now be a value, and each value should be a key. 
# Assume both the keys and values of the dictionary are immutable.
#
# EXAMPLE:
my_dict = {
  "A": "B", 
  "C": "D",
  "E": "F"
}
#
# invert(my_dict) => {'B': 'A', 'D': 'C', 'F': 'E'}

def invert(dic):

    invert_dic = {}

    for key, value in dic.items():
        invert_dic[value] = key
    
    return invert_dic

print(invert(my_dict))

print()
print("----- Ejercicio ---- \n")
# Declare a count_of_value function that accepts a dictionary and an integer.
# It should return a count of the number of times the integer appears 
# as a value among the dictionary’s values.
#
# EXAMPLE:
my_dict2 = { "a" : 5, "b" : 3, "c" : 5 }
#
# count_of_value(my_dict, 5) => 2
# count_of_value(my_dict, 3) => 1

def count_of_value(dic, integer):
    cont = 0
    for _, value in dic.items():
        if value == integer:
            cont += 1
    return cont

print(count_of_value(my_dict2, 5))
print(count_of_value(my_dict2, 3))


print()
print("----- Ejercicio ---- \n")
# Declare a sum_of_values function that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
#
# The function should return the sum of values for dictionary 
# keys that are also found in the list.
#
# NOTE: sum is a reserved keyword in Python. Don’t use it as a variable name.
#
# EXAMPLES:
my_dict3 = { "a": 5, "b": 3, "c": 10 }
#
# sum_of_values(my_dict, ["a"])            => 5
# sum_of_values(my_dict, ["a", "c"])       => 15
# sum_of_values(my_dict, ["a", "c", "b"])  => 18
# sum_of_values(my_dict, ["z"])            => 0

def sum_of_values(dic, list):
    suma = 0
    for letter in list:
        if letter in dic:
            suma = suma + dic[letter]
        
    return suma
    
print(sum_of_values(my_dict3, ["a"]))
print(sum_of_values(my_dict3, ["a", "c"]))
print(sum_of_values(my_dict3, ["a", "c", "b"]))
print(sum_of_values(my_dict3, ["z"]))