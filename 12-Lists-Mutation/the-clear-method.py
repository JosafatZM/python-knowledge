# Literally clears the whole list 

citrus_fruits = ["Lemon", "Orange", "Lime"]
citrus_fruits.clear()
print(citrus_fruits) # Gives us back an empty list []

print()
# Declare a delete_all function that accepts a list of strings and a target string
# Remove all occurrences of the target string from the list and return it
#
# EXAMPLES
# delete_all([1, 3, 5], 3)  => [1, 5]
# delete_all([5, 3, 5], 5)  => [3]
# delete_all([4, 4, 4], 4)  => []
# delete_all([4, 4, 4], 6)  => [4, 4, 4]

# Esta solucion no fue posible porque el for al hacer el loop y eliminar un
# elemento hace una nueva lista y ya no revisa el index 0 por eso al hacerlo asi
# quedaba una lista con un numero al final 

#  def delete_all(list, string):
#     for elements in list:
#         if elements == string:
#             list.remove(string)
#     return list
def delete_all(list, string):
    while string in list:
        list.remove(string)
    return list

print(delete_all([1, 3, 5], 3)) 
print(delete_all([5, 3, 5], 5))
print(delete_all([4, 4, 4], 4))
print(delete_all([4, 4, 4], 6))

print()
# Declare a push_or_pop function that accepts a list of numbers
# Build up and return a new list by iterating over the list of numbers
# If a number is greater than 5, add it to the end of the new list
# If a number is less than or equal to 5, remove the last element added to the new list
# Assume the order of numbers in the argument will never require removing from an empty list
#
# EXAMPLES
# push_or_pop([10])            => [10]
# push_or_pop([10, 4])         => []
# push_or_pop([10, 20, 30])    => [10, 20, 30]
# push_or_pop([10, 20, 2, 30]) => [10, 30]

def push_or_pop(list):
    new_list = []
    cont = 0
    for elements in list:
        if elements > 5:
            new_list.append(elements)
        else:
            new_list.pop()
    return new_list

print(push_or_pop([10, 4]))
print(push_or_pop([10]))
print(push_or_pop([10, 20, 30]))
print(push_or_pop([10, 20, 2, 30]))


nums = [1,2, 2, 2, 4]
val = 2

a = [num for num in nums if num != val]

print(a)
