units = ["meter", "kilogram", "second", "ampere", "kelvin", "candela", "mole"]

more_units = units.copy()

# print(units)
# print(more_units)

units.remove("mole")
print(units)
print(more_units)

# Otra manera de generar la copia de una lista es...

even_more_units = units[:]
print(even_more_units)


