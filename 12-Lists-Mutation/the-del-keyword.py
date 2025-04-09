# Eliminates a range of index of the list you indicate
soups = ["Chiken Noodle", "French Onion", "Clam Chowder", "Miso", "Wonton"]

# del soups[1]
# del soups[-1] # You delete the last elemento of the list  
del soups[:] # The second is exclusive means you only delete index 1 & 2

print(soups)

prueba = ("hola", 23, "%345")
# del prueba[1]
# TypeError Tuple object does not support item deletion 
# del prueba[:]
# print(prueba)