# Creates a list based on the argument you give to the method
# String ==> List
names = "Josafat, Paula, Alondra, Frida, Jorge, Pablo, Daniel, Monsesita, Meli, Diego, Renata"

print(names.split(", "))
# Space 
print()

print(names.split(", ", 4)) # The number of cuts that you want to do

sentence = "Python is such a great languaje for programming"
number_of_words = sentence.split(" ")

print(len(number_of_words))

print()
# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
#
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut")   => [8, 5, 2, 5]

# PREMIO POR HACERLO A LA PRIMERA DE MANERA ELEGANTE 
def word_lengths(sentence):
    
    words = sentence.split(" ")
    length_of_words = []

    for word in words:
        length_of_words.append(len(word))

    return length_of_words

print(word_lengths("Mary Poppins was a nanny"))
print(word_lengths("Somebody stole my donut"))


print()
# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"])           => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"])  => "cat er pillar"
# cleanup(["", "", " "])                     => ""

def clean_up(list):

    final_string = []

    i = 0 
    while i < len(list):
        
        if "" in list:
            list.remove("")
        if " " in list:
            list.remove(" ")

        i += 1
    
    final_string = " ".join(list)
    
    return final_string

print(clean_up(["cat", " ", "er", "", "pillar"]))
print(clean_up(["cat", " ", "er", "", "pillar"]))
print(clean_up(["", "", " "])  )

print()
# FORMA ELEGANTE E INTELIGENTE 

def cleanup(list):
    clean_string = []

    for strings in list:
        if strings.isspace() or len(strings) == 0:
            continue

        clean_string.append(strings)
    
    return " ".join(clean_string)

print(cleanup(["cat", " ", "er", "", "pillar"]))
print(cleanup(["cat", " ", "er", "", "pillar"]))
print(cleanup(["", "", " "])  )

