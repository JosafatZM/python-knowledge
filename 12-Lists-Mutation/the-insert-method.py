# Inserts an element on a given index position 
from tkinter import Place


plays = ["Hamlet", "Macbeth", "King Lear"]

plays.insert(1, "Julius Caesar")
print(plays)

plays.insert(0, "Romeo & Juliet")
print(plays)


# This one work like the append method
plays.insert(10, "A Midsummer Night's Dream")
print(plays)

plays.append("Hola")
print(plays)

print()
# Write a factors function that accepts a positive whole number
# It should return a list of all of the number's factors in ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?
#
# EXAMPLES
# factors(1)  => [1]
# factors(2)  => [1, 2]
# factors(10) => [1, 2, 5, 10]
# factors(64) => [1, 2, 4, 8, 16, 32, 64]

def factors(number) -> int:
    list = []
    contador = 0 
    while contador < number:
        contador += 1
        if number % contador == 0:
            list.append(contador)

    return list 

print(factors(64))

def factores(numero) -> int:
    lista = []
    for numeros in range(1,numero + 1):
        if numero % numeros == 0:
            lista.append(numeros)
    return lista

print(factores(64))

