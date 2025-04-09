def positive_or_negative(number):
    if number > 0:
        return "Positivo"
    elif number < 0:
        return "Negativo"
    else: 
        return "Ninguno de los dos porque es 0"

print(positive_or_negative(5))
print(positive_or_negative(0))
print(positive_or_negative(-9))

print()

def calculadora(operacion, a ,b):
    if operacion == "add":
        return a + b
    elif operacion == "substract":
        return a - b
    elif operacion == "multiply":
        return a * b
    elif operacion == "divide":
        return a/b
    else:
        return "I dont know what you want me to do"

print(calculadora("add",6,7))
print(calculadora("substract",6,7))
print(calculadora("multiply",6,7))
print(calculadora("divide",6,7))
print(calculadora("transmogrify",6,7))

print()

# Ejercicio 
# Declara negative_energy function thath accepts a numeric argument 
# and returns its absolute value.
# The absolute value is the number's distance from zero.
#
# negative_energy(-5) => 5
# negative_energy(5) => 5
# negative_energy(0) => 0

def negative_energy(numero):
    if numero >= 0:
        return numero
    elif numero < 0:
        return -numero

print(negative_energy(-5))
print(negative_energy(5))
print(negative_energy(0))