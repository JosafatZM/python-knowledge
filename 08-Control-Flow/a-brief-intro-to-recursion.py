# def reverse(str):
#     start_index = 0
#     last_index = len(str) - 1 
#     reversed = ""

#     while last_index >= start_index:
#         reversed += str[last_index]
#         last_index -= 1

#     return reversed

# USANDO RECURSION 



def reverse(str):
    if len(str) <= 1:
        return str

    return str[-1] + reverse(str[:-1])
# ASI ES COMO FUNCIONA 
# hola
# a + reverse(hol)
# a + l + reverse(ho)
# a + l + o + reverse(h)
# a + l + o + h
def voltear(str):
    return str[::-1]

print(reverse("straw")) 
print(reverse("hola"))
print(voltear("pala"))

# Tarea usando recursion / dar el calculo factorial ! de un numero 

def factorial(num):
    if num == 1:
        return num

    return num * factorial(num - 1) 

# ASI FUNCIONA
#   return 5(El primer input) * factorial(4) <= que es el input - 1
#       return 4 * factorial(3)
#           return 3 * factorial(2)
#               return 2 * factorial(1)
# El if se hace TRUE y pasa esto
#               return 2 * 1
#           return 3 * 2
#       return 4 * 6
#   return 5 * 24
# return 120


print(factorial(3))
print(factorial(5))

print()