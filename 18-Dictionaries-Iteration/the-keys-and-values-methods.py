cryptos = {
    "Bitcoin": 40000,
    "Etherium": 2000,
    "XRP": 1
}

print(cryptos.values())

# Espacio
print()

print(cryptos.keys())

# Espacio
print()

print(type(cryptos.keys()))

# Como se itera a estos objetos

for key in cryptos.keys():
    print(f"The key is {key}")

# Espacio
print()

for value in cryptos.values():
    print(f"The value is {value}")

# Espacio
print()

# Conocer si un Value o Key existen en un Dictionarie
print("Rappi Coin" in cryptos.keys())
print("XRP" in cryptos.keys())
print(234 not in cryptos.values())

# Espacio
print()

# Conocer los key-value pairs the un Dictionarie
print(len(cryptos.values()))

# print("\n ----- Ejercicio -----")
# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# EXAMPLE:
my_dict = {
  "A": "K",
  "B": "D",
  "C": "A",
  "D": "Z"
}
#
# common_elements(my_dict) => ["A", "D"]

def common_elements(dic):
    
    result = []

    for word in dic:
        if word in dic.keys() and word in dic.values():
            result.append(word)
    
    return result

print(common_elements(my_dict))

# MANERA COOL 

def elementos_en_comun(dic):
    
    return [key for key in dic.keys() if key in dic.values()]


print(elementos_en_comun(my_dict))