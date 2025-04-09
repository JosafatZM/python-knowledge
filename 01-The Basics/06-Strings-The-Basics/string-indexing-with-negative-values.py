variable = "programacion"

print(variable[-1])
print(variable[-2])

#Taarea

def same_first_and_last_letter(text:str):
    return text[0] == text[-1]

print(same_first_and_last_letter("hola"))

def tree_number_sum(numeros:str):
    return (int(numeros[0]) + int(numeros[1]) + int(numeros[2]))

print(tree_number_sum("567"))

#Experimento josa

def primera_y_ultima_letra(word:str):
    return word[0] + word[-1]

print(primera_y_ultima_letra("bebe"))


#experimento comparando si la primera y la ultima letra son lo mismo 

def experimento_2(word:str):
    return word[0] == word[-1]

print(experimento_2("hola"))