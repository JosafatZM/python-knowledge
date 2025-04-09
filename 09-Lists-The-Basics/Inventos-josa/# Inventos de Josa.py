# Inventos de Josa
# Las Niñas Que Me Han Gustado finderxd

lista_de_exs = ["Paula", "Frida", "Fernanda", "Isis", "Mafer"]

print(" Bienvenido al \"Las Niñas Que Me Han Gustado finderxd\"")
print("\n Bueno esta cosa consiste en que si adivinas el nombre\
     \n de todas sus ex\'s ganas una paleta!!")
print(" Funfact \"Son 5\"")

# Contador de puntos y vidas 
puntos = 0
vidas = 3

# Variable para guardar el ultimo imput del usuario 
# para ver que despues no lo repita
last_imput = ""

# Para que no repita a una ex que ya se habia adivinado 
contador_adivinadas = 0 
adivinadas = ["", "", "", "", ""]

# Bienvendio al Juego 
print("\nBueno... Comenzemos!!!")

#Loop principal
while vidas > 0 and puntos < 5:
    # Aqui se pide el nombre de las susodichas
    user_input = input("\n Dame el nombre de una niña \nque le haya gustado a Josa: ")

    # Se limpia el input del usuario 
    user_input = user_input.title().strip()

    if user_input in lista_de_exs and user_input == last_imput:

        print("\n PERRO NO SE VALE REPETIR!!")
    elif user_input in adivinadas:

        print("\n PERRO NO SE VALE REPETIR!!")
    elif user_input in lista_de_exs:

        puntos += 1

        print(f" Correcto {user_input} es una ex de Josa, Ganaste un punto!!\
            \n Total de puntos: {puntos} \n Total de vidas: {vidas}")

        adivinadas[contador_adivinadas] = user_input
        contador_adivinadas += 1
    elif user_input not in lista_de_exs:

        vidas -= 1

        print(f" No inventes Josa jamas ha salido con una {user_input}, also\
            \n pierdes una vida por mentirosx!!\
            \n Total de puntos: {puntos} \n Total de vidas: {vidas}")

    last_imput = user_input

if vidas == 0:
    print("\n PERROOOO!! COMO ASI?!? Que no conoces los nombres de mis ex\'s \n")
else:
    print("\n TE AMO PERRO TE LAS SABES TODAAAAAS!!")