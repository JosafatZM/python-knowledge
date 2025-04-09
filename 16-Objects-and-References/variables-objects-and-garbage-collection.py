# A "variable" is just a pointer, a name an address an identifier, a reference
# for an object in our programs
#
# Garbage Collection: 
# Is the process by which the language cleans up or disposes of 
# any leftover garbage. garbage (objects that no longer are being used)

a = 1
a = True
a = ("Zamora", "Josafat", "Estudiante")

# ***Just an experiment***
#
# *nombre, ocupacion = a
# lista_de_nombre = list(map(lambda palabra: palabra, nombre))

# nombre_bien = " ".join(lista_de_nombre)
# print(nombre_bien)

# print(ocupacion)

a = True
# it's just going to print a cause' the other 
# values are garbage right now 
print(a)




