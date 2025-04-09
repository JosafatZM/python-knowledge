empty = []
empty = list()

sodas = ["coke", "pepsi", "Dr. pepper"]
print(len(sodas))

quarterly_revenues = [15000, 12000, 9000, 20000]
print(len(quarterly_revenues))

stock_prices = [13, 34, 56, 89, 100, 345]
print(len(stock_prices))

# Ejercicios de Tarea
#
# Create an empty list and assing it to the variable "empty".

empty = []

# Create a list with a single boolean - True - and 
# assing it to the variable "active"

active = [True]

# Create a list with 5 integers of your choice and 
# assing it to the variable "favorite_numbers"

favorite_numbers = [1, 3 , 6, 7 , 8]

# Declare an is_long function that accepts a single list as an argument 
# it should return True if the list has more than 5 elements, and false otherwise

def is_long(list):
    if len(list) > 5:
        return True
    else:
        return False

# MANERA EPICAMENTE ELEGANTE (es lo mismo que erriba pero mucho mas simple)

def elegante(element):
    return len(element) > 5

lista1 = [1, 2]
lista2 = [1, 2, 3, 4, 5, 6]

print(is_long(lista1))
print(is_long(lista2))
print()
print(elegante(lista1))
print(elegante(lista2))