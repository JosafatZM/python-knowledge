# El comando "type" te dice el tipo de cosa que es por ejemplo si es un
# int o si es un float o un str y los puedes usar en booleans para
# comparar si son de la misma clase 

print(type(5))
print(type(10))

print(type(1.8))
print(type(5.8))

print(type("computer"))
print(type("laptop"))

print(type(5) == type(10)) #aqui el autput es TRUE porque esta comparando el blueprint del que esta hecho no los numero en si
print(type("computer") ==  type("laptop"))
print(type(5) == type(5.0))
print(type(5) == type("5"))

print(type(True))
print(type(False))
print(type(False) ==type(True))
print(type(False)  != type(6))

#the bluperint es la class a la cual pertenecen cada uno de los argumentos
  