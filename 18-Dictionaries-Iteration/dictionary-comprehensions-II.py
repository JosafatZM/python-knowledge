capitales = {
    "Tabasco": "Villahermosa",
    "Tlaxcala": "Tlaxcala",
    "Veracruz": "Xalapa",
    "Jalisco": "Guadalajara",
    "Nuevo Leon": "Monterrey",
    "Quintana Roo": "Chetumal",
    "Puebla": "Puebla"
}

inverted = { capital: estado for estado, capital in capitales.items() if len(capital) != len(estado)}

print(inverted)

# Espacio 1
print()

# Ejemplo del cuestionario 
sentences = [
  "Bobby went to the store on the corner",
  "Sally ate a candy bar",
  "Justin played on his deluxe piano"
]
 
word_counts = { sentence: len(sentence.split(" ")) for sentence in sentences }
print(word_counts)

# Espacio 2
print()

# Ejemplo del cuestionario
values = [1, 2, 3, 4, 5]
print({ value: sum(values[0:index + 2]) for index, value in enumerate(values) })

# Espacio 3
print()

print("\n----- Ejercicio -----\n")

# You are writing a Python program to model a remote control
# for a television set. Declare a stations_to_numbers
# function that accepts a dictionary. The keys will be
# channel numbers and the values will be the station names.
# For example...
channels = {
  2: "CBS",
  4: "NBC",
  5: "FOX",
  7: "ABC"
}
# The stations_to_numbers function should return an
# inverted dictionary where the keys are the station names
# and the values are the channel numbers
#
# stations_to_numbers(channels) => {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7}

def stations_to_numbers(dictionary):
    return { station: channel for channel, station in dictionary.items() }

print(stations_to_numbers(channels))


print("\n----- Ejercicio -----\n")

# Declare a coaster_conversion function that accepts a dictionary
# The keys of the dictionary will be strings representing roller coasters
# The values will be the heights of each coaster in meters
#
# Return a new dictionary with the same keys.
# The values should be the heights converted from meters to feet,
# The final values (in feet) should also be rounded to the closest integer
# HINT: 1 meter is equal to 3.28084 feet
# HINT: The round function rounds a number to the nearest integer
#
coasters = {
  "Kingda Ka": 139,
  "Top Thrill Dragster": 130,
  "Superman: Escape From Krypton": 126
}
#
# coaster_conversion(coasters) => {'Kingda Ka': 456, 'Top Thrill Dragster': 426, 'Superman: Escape From Krypton': 413}

def coaster_conversion(dictionary):
    return {key: round(value * 3.28084) for key, value in dictionary.items()}

print(coaster_conversion(coasters))

# Ultimo espacio
print()

# Given the list below, write a dictionary comprehension to return a 
# dictionary where the keys are the numbers and the values are their cubes.
# The dictionary should only use the numbers that are even.

numbers = [3, 6, 7, 12, 15]

result = { number: number**3 for number in numbers if number %2 == 0}
print(result)