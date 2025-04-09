# The add.() method adds a single element
disney_characters = {
    "Hanna Montana",
    "Olaf",
    "Mickey Mouse"
}

disney_characters.add("Donald")
print(disney_characters)

print()

# The update.() method adds multiple elements

# this goes through every single element in the iterable (element)
disney_characters.update(["Muppets", "LionKing"])
print(disney_characters)

disney_characters.update(("Simba", "Pluto"))
print(disney_characters)