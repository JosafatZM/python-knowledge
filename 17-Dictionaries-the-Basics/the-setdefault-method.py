# Diferences
# If a key is not found in a dictionary, the get method will return its 
# second argument as the value. In comparison, if a key is not found in 
# a dictionary, the setdefault method writes the key-value pair to the dictionary.
# The first argument to the method will serve as the key and the second argument 
# will serve as the value. The second argument has a default argument of None.


film_directors = {
    "The Godfather": "Francis Ford Coopola",
    "The Rock": "Michael Bay",
    "Pretend it's a city": "Martin Scorsese"
}

print(film_directors.get("The Rock"))
print(film_directors.get("Bad Boys", "Michael Bay"))
print(film_directors.get("Bad Boys"))
print(film_directors)

print()

# If you don't assing it a values it takes the value of none
film_directors.setdefault("Bad Boys")
print(film_directors)
print() # Espacio
# Only takes the first if it doesn't find the argument (Key)
film_directors.setdefault("Bad Boys", "Josafat Zamora")
print(film_directors)

print() # Espacio 
film_directors.setdefault("Bad Boys", "Josafat Zamora")
print(film_directors)

print("----- Ejercicio -----\n")

# Define a to_dictionary function that accepts a list of strings. 
# The function should return a dictionary where the keys are the strings 
# and the values are their original index positions in the list.
#
# EXAMPLE:
# detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
# to_dictionary(detectives) => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}

detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]

def to_dictionary(list):

    dictionary = {}

    for index, detective in enumerate(list):
        dictionary[detective] = index
    
    return dictionary

print(to_dictionary(detectives))

print("----- Ejercicio -----\n")

# Define a length_counts function that accepts a list of strings. 
# The function should return a dictionary where the keys represent
# length and the values represent how many strings have that length.
#
# EXAMPLE:
# sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
# length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
# There is 1 string with 6 letters, 2 strings with 9 letters, 
# 2 strings with 7 letters, and 1 string with 4 letters.

sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]

def length_counts(list):

    dicitonary = dict()

    for word in list:
        if len(word) not in dicitonary:
            dicitonary[len(word)] = 1
        elif len(word) in dicitonary:
            dicitonary[len(word)] += 1

    return dicitonary

print(length_counts(sa_countries))

# MANERA ELEGANTE??

def length_count_segun_boris(elements):
    counts = dict()

    for element in elements:
        length = len(element)
        current_count = counts.get(length, 0)
        counts[length] = current_count + 1
    
    return counts

print(length_count_segun_boris(sa_countries))