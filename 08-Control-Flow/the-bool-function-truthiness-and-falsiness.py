if 10 < 11:
    print("hello")

if 3:
    print("goodbye")

if -3:
    print("negatives are truethy")

if 0:
    print("this will not be printed")

if "hello":
    print("it will pe printed")

if "":
    print("this is false")

if 37>34:
    print("\n Hola josa")

# bool function works for whatever argument you give to the
# bool function if you are going to put this into an if statement is going
# to tell you if its going to be evaluated as true or false
print("\n")
print(bool(1)) #true
print(bool(0)) #false
print(bool("")) #false
print(bool("python")) #true
print(bool(3.14)) #true
print(bool(" ")) #true

# ejercicio 
print()
# numero par o impar 
def even_odd(numero: int):
    if numero % 2 == 0:
        return "even"

    return "odd"

print(even_odd(8))
print(even_odd(5))

# ejercicio 2
print()

def verdad_o_falso(word):
    if bool(word):
        return F"The value {word} is {bool(word)} "

    return f"The value {word} is falsy"

print(verdad_o_falso(0))
print(verdad_o_falso(5))