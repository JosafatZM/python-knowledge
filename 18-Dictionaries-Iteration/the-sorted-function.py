# Nomenclatura para usar sort en listas
numeros = [1, 2, 3, 4, 5]
print(sorted(numeros))
numeros.sort()
print(numeros)

# Espacio 1
# A patir de aqui se trabaja con dictionaries
print()
# Esto se puede extrapolar a los diccionarios

salaries = {
    "Execitive Assistant": 20,
    "CEO": 50,
    "animal": 0,
    "Mascota": 10

}

# Me imprime las Keys ordenas de forma 
# alfabetica 
print(sorted(salaries))

# Espacio 2
print()

# Imprime la lista completa
print(salaries)

# Espacio 3
print()

wheel_count = {
    "Truck": 12,
    "Car": 4,
    "Motor cicle": 2,
    "Bus": 8
    }

print(sorted(wheel_count.items()))


# Sintaxys para iterar en un dicionario de manera ordenada
for key, value in sorted(wheel_count.items()):

    print(f"The value is {key} and the key is {value}")

# Ejemplo mas especifico de iteracion sobre un diccionario ordenado 

print() # Espacio 4
abecedario = {
    "c": 3,
    "b": 2,
    "a": 1
}

for key, value in sorted(abecedario.items()):
    print(f"The value is \"{key}\" and the key is {value}")
    