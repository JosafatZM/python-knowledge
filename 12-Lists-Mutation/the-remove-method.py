# Deletes the first "Zelda"
nintendo_games = ["Zelda", "Mario", "Zelda", "Donkey Kong"]

nintendo_games.remove("Zelda")
print(nintendo_games)

nintendo_games.remove("Zelda")
print(nintendo_games)

if "Wario" in nintendo_games:
    nintendo_games.remove("Wario")

if "Mario" in nintendo_games:
    nintendo_games.remove("Mario")

print(nintendo_games)

nintendo_games.remove("Donkey Kong")
print(nintendo_games)

nombres_de_niñas_bonitas = ["Melissa", "Melissa", "Melissa"]

# SI NO SE LE ASIGA UN ARGUMENTO RECIVES UN TypeError DEBIDO A QUE NO 
# SE DIERON LOS ARGUMENTOS SUFICIENTES PARA LLEVAR A CABO LA ACCION

# nombres_de_niñas_bonitas.remove()
# print(nombres_de_niñas_bonitas)
