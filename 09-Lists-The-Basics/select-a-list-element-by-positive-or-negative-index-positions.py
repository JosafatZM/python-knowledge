
print("organic"[5])

web_browsers = ["Chrome", "Firefox", "Explorer", "Safari", "Opera", "Brave"]
print(web_browsers[3])
print(web_browsers[2])
print(web_browsers[4])

print()
print(web_browsers[4][1]) #Obtener un elemento dentro de un elemento de la lista

print()
presidentes = ["Amlo", "Peña", "Calderon", "Salinas"]
print(presidentes[-1]) #Para obtener el ultimo de la lista
print(presidentes[-2])
print(presidentes[-3])
print(presidentes[-4])
# print(presidentes[-5]) esto ya no se puede hacer

print()
# TAREA

# Define un a funcion que acepte una lista de strings
# la cual debera retornar una concatenacion del primer
# y ultimo elemento de la lista

def first_and_last(list):
    return list[0]+list[-1]

 
print(first_and_last(["hola ", "juan", "josa"]))
print(first_and_last(["c", "b", "a"]))
print(first_and_last(["a"]))



print()
# Define una funcion que acepte una lista de numeros
# Esta lista debera tener SIEMPRE 6 elementos
# la funcion debera retornar la multiplicacion de 
# todos los elementos de la lista que no sean pares

def product_of_even_indices(list):
    producto_final = [1,1,1,1,1,1,1]
    if list[0] % 2 != 0:
        producto_final[0] = list[0]
    if list[1] % 2 != 0:
        producto_final[1] = list[1]
    if list[2] % 2 != 0:
        producto_final[2] = list[2] 
    if list[3] % 2 != 0:
        producto_final[3] = list[3]
    if list[4] % 2 != 0:
        producto_final[4] = list[4]
    if list[5] % 2 != 0:
        producto_final[5] = list[5]
    return producto_final[0]*producto_final[1]*producto_final[2]*\
        producto_final[3]*producto_final[4]*producto_final[5]

print(product_of_even_indices([1,2,3,4,5,6]))
print(product_of_even_indices([3,4,3,5,3,6]))

print()
# Define una funcion que acepte una lista de numeros
# Esta lista debera tener SIEMPRE 6 elementos
# la funcion debera retornar la multiplicacion de 
# todos los elementos de la lista en posiciones pares

def multiplicacion_posiciones_pares(list):
    return list[0] * list[2] * list[4]

print(multiplicacion_posiciones_pares([1,2,3,4,5,6]))
print(multiplicacion_posiciones_pares([3,4,3,5,3,6]))

print()
# Define a fist_letter_of_last_string function that accepts a list of string.
# It should return one character - the first letter of the last string in the list.
# Assume the list will always have at least one string.

def firts_letter_of_last_string(list):
    return list[-1][0]

print(firts_letter_of_last_string(["nonesense"]))
print(firts_letter_of_last_string(["nonesense", "cat", "dod", "zebra"]))


print("\n ----- Ejercio Actualizado -----\n")
# Define una funcion que acepte una lista de numeros
# Esta lista debera tener SIEMPRE 6 elementos
# la funcion debera retornar la multiplicacion de 
# todos los elementos de la lista que no sean pares

lista_de_numeros = [1, 2, 3, 4, 5, 1]

def multiplicacion_de_la_lista(lista):

    producto = []

    for element in lista:
        if element % 2 == 0:
            producto.append(element)
            continue
    
    resultado = 0
    for element in producto:
        if element == producto[0]:
            resultado = element
            continue
        resultado = resultado * element
    
    return resultado
        

        

print(multiplicacion_de_la_lista(lista_de_numeros))
