
languages = ["Python", "JavaScript", "Ruby", "C++"]

lenghts = { language: len(language) for language in languages if "t" in language}
print(lenghts)

word = "holacomotellamasminombreesjosafatzamoramunoz"

# Espacio 1
print()

letter_count = { letter: word.count(letter) for letter in word}
print(letter_count)