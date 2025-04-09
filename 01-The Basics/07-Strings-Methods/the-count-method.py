word = "queueing"

print(word.count("e"))
print(word.count("u"))
print(word.count("q"))
print(word.count("z"))
print(word.count("Q"))

print(word.count("ue"))
print(word.count("ing"))
print(word.count("u")+ word.count("e"))

print()

#TAREA METHODS

def vowel_count(text):
    return text.count("a") +\
    text.count("e") +\
    text.count("i") +\
    text.count("o") +\
    text.count("u") 

print(vowel_count("helicopter"))


def find_my_letter(word,letter):
    return word.find(letter)

print(find_my_letter("hola josa aprende a usar otro ejemplo yaa", "a"))



def contador_de_letras(palabra,letra):
    return palabra.count(letra)


print(contador_de_letras("el otro dia fui a el parque", "i"))

print()

# A parti de aqui todos son experimetos 

def experimeto(a, b, c):
    return(a + b + c)

print(experimeto(9, 8, 4))    

def experimento_2(text, letras):
    return text.count(letras)

print(experimento_2("helicoptero", "i"))

def experimento_3(texto, letra):
    return texto.find(letra)

print(experimento_3("helicoptero","e"))

# hay un contador de vocales arriba que explica como hacer con 
# todas las vocales 

def encontrador_de_vocales(palabara,vocal):
    return palabara.count(vocal)

print(encontrador_de_vocales("Josafat", "i"))    