# import re
# from typing import Counter


# count = 0 

# while count < 5:
#     print(count)
#     count+=1
    

# print(count) 


# En python a diferencia de C puedes asignar un valor de True
# invalid_number = True

# while invalid_number:
#     user_value = int(input(f"Pleaes enter a number above 10: "))
#     if user_value > 10:
#         print(f"Yes {user_value} is a great number!")
#         invalid_number = False
#     else:
#         print("That does no fit, try again please...")


# Ejercicio FizzBuzz
# if is divisible by 3 Fizz
# "                " 5 Buzz
# "                " both of them FizzBuzz
# "                " none of them print the number

# print("-----------")
# def fizzbuzz(num):
#     cont = 0
#     while cont < num:
#         cont += 1 
#         if cont % 3 == 0 and cont % 5 == 0:
#             print("FizzBuzz")
#         elif cont % 3 == 0 and cont % 5 != 0:
#             print("Fizz")
#         elif  cont % 3 != 0 and cont % 5 == 0:
#             print("Buzz")
#         else:
#             print(cont)


# def fizzbuzz(number):
#     count = 0
#     while count < number:
#         count += 1
#         if count % 3 == 0 and count % 5 == 0:
#             print("FizzBuzz")
#         elif count % 3 == 0 and count % 5 != 0:
#             print("Fizz")
#         elif  count % 3 != 0 and count % 5 == 0:
#             print("Buzz")
#         else:
#             print(count)
#     return


# print(fizzbuzz(23))

#------- Nuevo Repazo 15/03/22 --------

# count = 0

# while count < 5:
#     count += 1 # -> es como poner count = count + 1
#     print(count)
    


# invalid_number = True

# while invalid_number:
#     user_value = int(input("Ingresa un numero mayor a 10: "))
#     if user_value > 10:
#         print(f"Excelente!! {user_value} es un gran numero!!")
#         invalid_number = False
#     else:
#         print(f"Mm {user_value} no es mayor a 10... Vuelve a intentar!!")

# Problema FizzBuzz

def fizzbuzz(argumento):
    contador = 1
    while contador <= argumento:
        if contador % 3 == 0 and contador % 5 == 0:
            print("FizzBuzz")
        elif contador % 3 == 0 and contador % 5 != 0:
            print("Fizz")
        elif contador % 3 != 0 and contador % 5 == 0:
            print("Buzz")
        else:
            print(contador)
        contador += 1


fizzbuzz(99)