print(sum([1, 3, 6, 7, 9, 2, 3])) # only int
print(sum([1, 1.1, 3.5, 5, 7.8, 4, 4.3, 2.6])) # convined
print(sum([1.0, 3.5, 5.5, 6.4, 2.6, 3.5, 3.0])) # only float



print()
print("\n***** Ejercicio *****\n")
# Declare a greater_sum function that accepts two lists of numbers.
# It should return the list with the greatest sum.
# You can assume the lists will always have different sums.
#
# EXAMPLES
# greater_sum([1, 2, 3], [1, 2, 4]) => [1, 2, 4]
# greater_sum([4, 5], [2, 3, 6])    => [2, 3, 6]
# greater_sum([1], [])              => [1]

# def greater_sum(list1, list2):

#     biggest_sum = []

#     if sum(list1) > sum(list2):
#         biggest_sum = list1
#     else:
#         biggest_sum = list2
    
#     return biggest_sum

# Manera mas elegante

def greater_sum(list1, list2):

    if sum(list1) > sum(list2):
        return list1
    
    return list2

print(greater_sum([1, 2, 3], [1, 2, 4]))
print(greater_sum([4, 5], [2, 3, 6]))
print(greater_sum([1],[]))



print()
print("\n***** Ejercicio *****\n")
# Declare a sum_difference function that accepts two lists of numbers.
# It should return the difference between the sum of values in the first list and the second list
#
# EXAMPLES
# sum_difference([1, 2, 3], [1, 2, 4]) => 6 - 7 => -1
# sum_difference([4, 5], [2, 3, 6])    => 9 - 11 => -2
# sum_difference([1], [])              => 1

def sum_difference(list1, list2):

    return sum(list1) - sum(list2)

print(sum_difference([1, 2, 3], [1, 2, 4]))
print(sum_difference([4, 5], [2, 3, 6]))
print(sum_difference([1], []))