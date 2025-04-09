# Agregas un elemento mas al final de la lista 

countries = ["United States", "Canada", "Mexico"]
print(countries)
print(len(countries))
print()

countries.append("Japon")
print(countries)
print(len(countries))
print()

countries.append("France")
print(countries)
print(len(countries))
print()

# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# EXAMPLES
# length_match(["cat", "dog", "kangaroo", "mouse"], 3))  => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5))  => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4))  => 0
# length_match([], 5))                                   => 0

def length_match(lista, integer):
    contador = 0

    for argument in lista:
        if len(argument) == integer:
            contador += 1 

    return contador

print(length_match(["cat", "dog", "kangaroo", "mouse"], 3))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 5))
print(length_match(["cat", "dog", "kangaroo", "mouse"], 4))
print(length_match([],5))

print()
# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).
#
# EXAMPLES
# sum_from(1, 2)   # 1 + 2                  => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5      => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8  => 33
# sum_from(9, 12)  # 9 + 10 + 11 + 12       => 42

def sum_from(start, end):
    total = 0

    for number in range(start, end + 1):
        total += number

    return total

print()
# Declare a same_index_values function that accepts two lists.
# The function should return a list of the index positions in which the two lists have equal elements
#
# EXAMPLES
# same_index_values([1, 2, 3], [3, 2, 1])                         => [1]
# same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"])   => [1, 3]

# Metodo de Josa
# def same_index_values(list_1, list_2):
#     final_list = []

#     for index, element in enumerate(list_1):
#         for index_2, element_2 in enumerate(list_2):
#             if index == index_2 and element == element_2:
#                 final_list.append(index)
        
#     return final_list


# Metodo Elegante
def same_index_values(list1, list2):
    results = []

    for index, values in enumerate(list1):
        if values == list2[index]:
            results.append(index)
    
    return results

print(same_index_values([1, 2, 3], [3, 2, 1]))
print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))