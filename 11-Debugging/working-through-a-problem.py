# Define a function tha iterates over a list of numbers,
# miltiplies each number by one less than its index position 
# and returns the total sum of those products

# Metodo de Josafat 
# lista = [1, 2, 3, 4, 5]

# def suma_de_productos(list):
#     total = 0
#     for index,num in enumerate(list):
#         total = total + num * (index-1)
#     return total

# print(suma_de_productos(lista))

# Metodo visto en el curso
# 1 * (0-1) = -1
# 2 * (1-1) = 0
# 3 * (2-1) = 2
# 4 * (3-1) = 8
# 5 * (4-1) = 15
# ==============
# Total = 25

lista_de_numeros = [1, 2, 3, 4, 5]

def multiply_element_by_one_less_than_index(lista_de_numeros):
    total = 0
    for index, number in enumerate(lista_de_numeros):
        total += number * (index - 1)
    return total

print(multiply_element_by_one_less_than_index(lista_de_numeros))