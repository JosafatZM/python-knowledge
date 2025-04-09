from calendar import month
from queue import Empty


print(set([1, 2, 3]))
print(set([1, 2, 3, 1 ,25 , 6, 25]))

# Espacio 1
print()

# convert a tuple into a set
print(set((1, 2, 3)))
print(set((1, 2, 3, 1, 2, 3)))

# Espacio 2
print()

print(set("abc"))
print(set("aabbnnccczzzxx"))

# Espacio 3
print()

# Convert a dictionary into a set
print(set({"key": "value"}))

# Espacio 4
print()

# Eliminate duplicates form a list
philosophers = ["Josafat", "Monse", "Daniel", "Jair", "Meli", "Josafat"]

philosophers_set = set(philosophers)

philosophers = list(philosophers_set)

print(philosophers)

print("\n----- Ejercicio -----\n")
# Ejercicio 
# Declare a set with 3 of your favorite movies as strings.
# Assign it to a movies variable.
movies = {"Titanic", "El pianista", "El hoyo"}

# Declare a set with the first four months of the year as strings.
# Assign it to a months variable.
# Make sure the first letter of each month is capitalized.
months = {"January", "February", "March", "April"}

# Create an empty set and assign it to an empty variable.
empty = set()

# Define a remove_duplicates function that accepts a single list as an argument. 
# The function should return a list with all of the duplicates from the original list removed. 
# The order of elements in the returned list is irrelevant.
#
# EXAMPLES:
# remove_duplicates([1, 2, 1, 2])  => [1, 2] or [2, 1]
# remove_duplicates([1, 2, 3, 4])  => [1, 2, 3, 4] in some order

def remove_duplicates(lista):
    lista_to_set = set(lista)
    set_to_lista = list(lista_to_set)
    return set_to_lista

# Forma elegante

def eliminar_duplicados(elementos):
    return list(set(elementos))

print(eliminar_duplicados([1, 2, 1, 2]))