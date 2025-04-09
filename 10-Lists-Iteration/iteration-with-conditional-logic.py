from unicodedata import numeric


values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]

def odds_sum(number):
    total = 0
    for n in number:
        if n % 2 != 0:
            total += n
    return total

print(odds_sum(values))
print(odds_sum(other_values))

print()
# Como lo hice yo 
def greatest_number(lista):
    greatest = 0
    counter = 0
    for numero in lista: 
        if lista[counter] > lista[counter-1]:
            greatest = lista[counter]
        counter += 1

    return greatest

# Manera mas simplificada
def instructor_mode(lista):
    greatest = lista[0]
    for number in lista:
        if number > greatest:
            greatest = number
    return greatest

print(greatest_number([1, 3, 5 , 2]))
print(greatest_number([1, 2, 3, 4]))
print(greatest_number([4, 3, 2, 1]))
print(greatest_number([-4, -3, -2, -1]))

print()

print(instructor_mode([1, 3, 5 , 2]))
print(instructor_mode([1, 2, 3, 4]))
print(instructor_mode([4, 3, 2, 1]))
print(instructor_mode([-4, -3, -2, -1]))

print()
# Define a smallest_number function  that accepts a list of numbers.
# It should return the smallest value in the list.
#
# smallest_number([1, 2, 3])     => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3

def smallest_number(list):

    smallest = list[0]

    for number in list:
        if number < smallest:
            smallest = number
    
    return smallest

print(smallest_number([1, 3, 5 , 2]))
print(smallest_number([0, 2, -76, 4]))
print(smallest_number([4, -7, 2, 1]))
print(smallest_number([-4, -3, -2, -1]))

print()
# Define a concatenate function that accepts a list of strings. 
#
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters.
#
# concatenate(["abc", "def", "ghi"])      => "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => ""

def concatenate(list):
    final_string = ""
    for string in list:
        if len(string) > 2:
            final_string += string
    return final_string

print(concatenate(["abc", "def", "ghi"]))
print(concatenate(["abc", "de", "fgh", "ic"]))
print(concatenate(["ab", "cd", "ef", "gh"]))

print()
# Define a super_sum function that accepts a list of strings. 
# The function should sum the index positions of the first occurence of the letter “s” in each word. 
#
# Not every word is guaranteed to have an “s”.
# Don’t use "sum" as a variable name as it’s a built-in keyword.
#
# super_sum([])                                 => 0
# super_sum(["mustache"])                       => 2
# super_sum(["mustache", "greatest"])           => 8
# super_sum(["mustache", "pessimist"])          => 4
# super_sum(["mustache", "greatest", "almost"]) => 12

# Se usa .find("s")

def super_sum(list):
    total = 0 
    for index in list:
        total += index.find("s")
    return total

print(super_sum([]))                                
print(super_sum(["mustache"]))
print(super_sum(["mustache", "greatest"]))
print(super_sum(["mustache", "pessimist"]))
print(super_sum(["mustache", "greatest", "almost"]))