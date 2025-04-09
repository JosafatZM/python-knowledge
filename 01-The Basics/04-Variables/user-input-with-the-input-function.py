#a = input("HELLO como te llamas?")
#print("un gusto conocerte", a)

#print("hola amigo dejame ayudarte a hacer unas sumas")
# b = input("dame un numero del 1 al 10  ")
# bebe = input ("dame un numero diferente al anterior  ")
# print("El total es", int(b) + int(bebe))


print("HOLA hoy te ayudare a convertir grados fahrenheit a celcius")
fahrenheit = input("Cuantos grados te gustaria convertir?")
print("El total es ", ((int(fahrenheit) - 32) * (5/9)))

#la manera mas elegante
user_value = input("Enter a temperature in Fahrenheit to convert to Celsius")
fahr_temp = float(user_value)
cles_tmep = (fahr_temp - 32) * (5/9)
print(fahr_temp, "in celsius is ", cles_tmep)


valor_del_usuario = input("hola dame 3 numero juntos que quieras sumar (Nota: no pongas espacios entre los numero por favor)")
a = (int(valor_del_usuario[0]) + int(valor_del_usuario[1]) + int(valor_del_usuario[2]))
print("el resultado de tu suma es",a)


