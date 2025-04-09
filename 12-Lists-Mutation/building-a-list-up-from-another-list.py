
powerball_numbers = [4, 8, 15, 16, 23, 42]

def squares(numbers):
    square_list = []

    for number in numbers:
        square_list.append(number ** 2)
    
    return square_list


print(squares(powerball_numbers))

def convert_to_float(numbers):
    float_list = []

    for number in numbers:
        float_list.append(float(number))

    return float_list

print(convert_to_float(powerball_numbers))

def even_or_odd(numbers):
    list_of_bool = []
    for number in numbers:
        list_of_bool.append(bool(number % 2 == 0))
    return list_of_bool

print(even_or_odd(powerball_numbers))

print()
#Tarea 
# Define an only_evens function that accepts a list of numbers. 
# It should return a new list consisting of only the even numbers from the original list.
#
# EXAMPLES
# only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
# only_evens([1, 3, 5])              => []
# only_evens([])                     => []

def only_even(list):
    even_list = []

    for number in list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

print(only_even([4, 8, 15, 16, 23, 42]))
print(only_even([1, 3, 5]))
print(only_even([]))

print()
# Define a long_strings function that accepts a list of strings. 
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# EXAMPLES
# long_strings(["Hello", "Goodbye", "Sam"])  => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"])        => []
# long_strings([])                           => []

def long_strings(list):
    long_strings = []

    for string in list:
        if len(string) >= 5:
            long_strings.append(string)
    
    return long_strings

print(long_strings(["Hello", "Goodbye", "Sam"]))
print(long_strings(["Ace", "Cat", "Job"]))


# def saludos_cordiales_para_monse():
#     str = "Hola, Saludos cordiales! Monse Tqm"

#     return str

# print(saludos_cordiales())