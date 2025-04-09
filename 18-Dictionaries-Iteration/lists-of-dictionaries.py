Concert_attendees = [
    {"Nombre": "Josa", "Seccion": "Vip", "Price": 2500.00},
    {"Nombre": "Meli", "Seccion": "General", "Price": 1250.00},
    {"Nombre": "Monse", "Seccion": "Vip", "Price": 2500.00},
    {"Nombre": "Jair", "Seccion": "Banamex", "Price": 2000.00},
]



for attendee in Concert_attendees:
    for key, value in attendee.items():
        print(f"El {key} es {value}")

# Espacio 1
print()

josa_festival = [
    {"Artista": "Bad Bunny",
     "Caterin": [
        {"Indispensables": ["Chocolate", "m&m's"]}, 
        {"No Indispensables": ["Agua Fiji", "Hot dogs"]}
        ]
    },
    {"Artista": "Olivia Rodrigo",
     "Caterin": [
        {"Indispensables": ["Agua Fiji", "m&m's"]}, 
        {"No Indispensables": ["Choco milk", "Gummy bears"]}
        ]
    },
]

print(f"Lo indispensable en el caterin de Bad Bunny es")


print(josa_festival[0]["Caterin"][0]["Indispensables"])

# Espacio 2
print()

print("Cosas indispensables en el Caterin de Bad Bunny:")
for value in josa_festival[0]["Caterin"][0]["Indispensables"]:
    print(f"{value}")

# Ejercicio de practica 
print("\n ----- Ejercicio -----\n")

# Assign list of four dictionaries to a "complexity" variable below

# The first and third dicitionaries should have two key-value pairs
# For those dictionaries, the keys should be strings and the values should be Booleans

# The second and fourth dictionaries should have three key-value pairs
# For the dictionaries, the keys shoul be floats
# and the values should be list of strings.
# the list can be any lenght

complexity = [
    {
        "Uno": True,
        "Dos": True
    },
    {
        1.0: ["Numero", "Uno"],
        2.0: ["Numero", "Tres"],
        3.0: ["Numero", "Tres"]
    },
    {
        "Tres": False,
        "Cuatro": False
    },
    {
        4.0: ["Numero", "Cuatro"],
        5.0: ["Numero", "Cinco"],
        6.0: ["Numero", "Seis"]
    }
]