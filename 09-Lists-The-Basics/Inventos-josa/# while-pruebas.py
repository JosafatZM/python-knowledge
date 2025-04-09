# while-pruebas

lista_de_exs = ["Paula", "Frida", "Fernanda", "Isis", "Mafer"]

user_input = input("\n Dame el nombre de una ex de josa: ")
comprobador = 0
while comprobador == 0:
    if lista_de_exs[0].title() == user_input.title():
        comprobador = 2
    elif lista_de_exs[1].title() == user_input.title():
        comprobador = 2
    elif lista_de_exs[2].title() == user_input.title():
        comprobador = 2
    elif lista_de_exs[3].title() == user_input.title():
        comprobador = 2
    elif lista_de_exs[4].title() == user_input.title():
        comprobador = 2
    else:
        comprobador = 1

print(comprobador)
print(lista_de_exs[0].title())
print(user_input.title())
if comprobador == 2:
    print("Cool")