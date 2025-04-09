release_dates = {
    "Python": 1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007
}

year_of_java = release_dates.pop("Java")
print(year_of_java)
release_dates.pop("Go")
print(release_dates)

new_year = release_dates.pop("C++", 2000)
print(new_year)

# LA MANERA MÁS VERGA DE HACERLO PERO NO RETIEN EL VALOR ELIMINADO
del release_dates["Ruby"]
print(release_dates)

print("\n ----- Ejercicio ----- \n")
# Declare a delete_keys function that accepts two arguments:
# a dictionary and a list of strings. 
# For each string in the list, if the string exists as a dictionary key, 
# delete the key-value pair from the dictionary. 
#
# If the string does not exist as a dictionary key, avoid an error. 
# The return value should be the modified dictionary object.
#
# EXAMPLE:
my_dict = {
  "A": 1,
  "B": 2,
  "C": 3
}
#
strings = ["A", "C"]
# delete_keys(my_dict, strings) => {'B': 2}

def delete_keys(dictionary, list):

    for element in list:
        if element in dictionary:
            dictionary.pop(element)
    
    return dictionary

print(delete_keys(my_dict, strings))