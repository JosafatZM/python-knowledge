alfabeto = "abcdefghijklmnopqrstuvwxyz"

print(alfabeto[0:100])
print(alfabeto[0:10:2])
print(alfabeto[0:28:3])
print(alfabeto[:28:3])
print(alfabeto[0::3])
print(alfabeto[::3])

print(alfabeto[4:20:5])
print(alfabeto[-20:-8:5])

print(alfabeto[::-3])
print(alfabeto[::-2])
print(alfabeto[::-1]) #la manera de poner un string al reves

print("otup"[::-1])

#tarea

print("\n")

def first_tree_characters(text):
    return text[0:3]

print(first_tree_characters("dynasty"))

def last_five_characters(word):
    return word[-5:]

print(last_five_characters("dynasty"))

def is_palindrome(palabra):
    return palabra[::] == palabra[::-1]

print(is_palindrome("ana"))
print(is_palindrome("arturo"))