
agents = {
    "007",
    "Raul",
    "Jorge"
}

# We get an error if the value that we want to remove
# does not exist in our set
agents.remove("007")


# remove.() ALSO WORKS ON LISTS
# hola = ["Josafat", "Zamora", "Munoz"]

# hola.remove("Josafat")
# print(hola)

print(agents)


# Espacio 1
print()

nombres = {
    "Melissa",
    "Sanz",
    "Monse"
}


# nombres = [
#     "Melissa",
#     "Sanz",
#     "Monse"
# ]

# # discard.() DOESN'T works on lists
# nombres.discard("Sanz")
# print(nombres)

# if the argument does not exist we don't get an errro
nombres.discard("Melissa")
print(nombres)

nombres.discard("Antonio")
print(nombres)
