
pizzas = [
    "Mushroom",
    "Pepperoni",
    "Sausage",
    "Barbecue Chicken",
    "Pepperoni",
    "Sausage"
]

print(pizzas.index("Barbecue Chicken"))
# If you have 2 strings repeated you recieve the index of the first one
print(pizzas.index("Pepperoni"))
print(pizzas.index("Sausage"))

# If a value is not in the list python returns an Error 
# We can use an if to avoid this situation 

# The second argument I provide is the index where I want to start the search of the value
print(pizzas.index("Pepperoni", 2))
# Also the argument is inclusive 
print(pizzas.index("Sausage", 2))

print()
# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""

def encrypt_message(string):

    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    str_idx = []
    idx_in_alpha = []
    final_message = []

    i = 0
    while i < len(string):

        if string[i] in alfabeto:
            str_idx.append(string[i])
            idx_in_alpha.append(alfabeto.index(string[i]))

        i += 1

    j = 0
    string_final = ""
    while j < len(idx_in_alpha):

        if idx_in_alpha[j] == 24:
            j_2 = 0 
            string_final += alfabeto[j_2]
        elif idx_in_alpha[j] == 25:
            j_3 = 1 
            string_final += alfabeto[j_3]
        else:
            string_final += alfabeto[idx_in_alpha[j]+2]

        j += 1
    
    return string_final

print(encrypt_message("abc"))
print(encrypt_message("xyz"))
print(encrypt_message(""))

print()
# Manera elegante de resolver el problema 
# Also funciona para recorrer los espacios que sean 
def elegant_encrypted_message(message):
    alphabet = "abcdefghijqlmnopqrstuvwxyz"
    encrypted = ""

    for letter in message:
        encrypted_letter_index_position = (alphabet.index(letter) + 2) % 26
        encrypted += alphabet[encrypted_letter_index_position]

    return encrypted

print(elegant_encrypted_message("abc"))
print(elegant_encrypted_message("xyz"))
print(elegant_encrypted_message(""))

print(26 % 26)
print(27 % 26)