story = "once upon a time"

print(story.capitalize())
print(story.title())
print(story.upper())
print("HELLO".lower())
print("AbCdE".swapcase())
print("ANDRES MANUEL LOPEZ".lower().title())

story = story.title()
print(story)

print("\n")

# Parte de practica 

str_de_practica = "hola mi nombre es josa"

print(str_de_practica.title())
print(str_de_practica.upper())
print(str_de_practica.capitalize())

print("Hola Me Gusta La Programacion Orientada A Objetos".swapcase())
print(str_de_practica.lower())


print("\n")

#practica que no tiene que ver con este tema 
#Es una de esas funciones que he hecho como unas dos mil veces 

def son_iguales(a,b):
    return a == b 

print(son_iguales("anaa", "ana"))

def ana_es_igual_a_ana(a):
    return a == (a[::-1])

print(ana_es_igual_a_ana("kayak"))


una_variable = "kayak"
print(una_variable[::-1]) # POR ALGUNA EXTRAÑA RAZON
                          # PYTHON SOLO LO PONE AL REVES
                          # SI ESTA DE ESTA MANERA 
