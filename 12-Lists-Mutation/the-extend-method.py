# Adds a new element to the last index
mountains = ["Everest", "K2"]
print(mountains)
print()
mountains.extend(["Nevado de Toluca", "Lhotse"])
print(mountains)
print()
montanas_extras = ["Pico de Orizaba"]
mountains.extend(montanas_extras)
print(mountains)

# If I add an empty list python does nothing

steaks = ["Tunderloin", "Sirloin"]
more_steaks = ["Ribeye", "T-bone"]

my_meal = steaks + more_steaks
print()
print(my_meal)

print()
steaks += more_steaks
print(steaks)