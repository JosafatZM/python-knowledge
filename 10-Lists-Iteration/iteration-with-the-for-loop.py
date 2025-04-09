# iterable: if its elements can be stepped over one by one 

from traceback import print_tb


dinner = "Steak an Potatotes"

# for character in dinner:
#     print(character)

numbers = [2, 3, 4, 5 ,6]

for number in numbers:
    print(number ** 2)

print()

novelists = ["Octavio Paz", "Hemingway", "Steinbeck"]

for novelist in novelists:
    print(len(novelist))

print()
# los argumentos del for se guardan en la memoria 
print(novelist)
print(number)

print()
#Sumar todos los numero en la lista numbers
cont = 0

for number in numbers:
    cont += number

print(cont)

print()
# Define a sum_of_lengths function tha accepts a list of strings
# The function should return the sum of the string legnths 

def sum_of_lengths(lista):
    length = 0
    for word in lista:
        length += len(word)
    return length

lista = ["Hello", "Bob"]
lista2 = ["Nonsense"]
lista3 = ["Nonsense", "or", "confidence"]

print(sum_of_lengths(lista))
print(sum_of_lengths(lista2))
print(sum_of_lengths(lista3))

print()
# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value

def product(list):
    contador = 1
    for number in list:
        contador = contador * number
    return contador

lista1 = [1, 2, 3]
lista_2 = [4, 5, 6, 7]
lista_3 = [10]

print(product(lista1))
print(product(lista_2))
print(product(lista_3))