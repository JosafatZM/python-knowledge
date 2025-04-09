
# UNPACKING A TUPLE

employee = ("Bob", "Jhonson", "Manger" , 50)
# if a variable has a "*" python puts it into a list 

# We separate the values that are after the first 2 values into a list
first_name, last_name, *details = employee
print(first_name)
print(last_name)
print(details)

print()
# "           " values that are behind the last 2 values
*names, position, age = employee
print(names)
print(position)
print(age)

print()
# We put the values in the middle into a list 
name, *details, age = employee
print(name)
print(details)
print(age)

print()
# We put age into a list and the output results in a [50] single value list
# because it has the "*" (asterisk)
name, last_name, position, *age = employee
print(name)
print(last_name)
print(position)
print(age)

print()
*datos, edad = employee
print(datos)
print(edad)

print()
print("****** Ejercicio *******")
# Given the tuple below, destructure the three values and
# assign them to position, city and salary variables
# Do NOT use index positions (i.e. job_opening[1])
job_opening = ("Software Engineer", "New York City", 100000)
position, city, salary = job_opening
print(position)
print(city)
print(salary)

print("\n****** Ejercicio *******")
# Given the tuple below, 
# - destructure the first value and assign it to a street variable
# - destructure the last value and assign it to a zip_code variable
# - destructure the middle two values into a list and assign it to a city_and_state variable
address = ("35 Elm Street", "San Francisco", "CA", "94107")
street, *city_and_state, zip_code = address
print(street)
print(zip_code)
print(city_and_state)

print("\n****** Ejercicio *******")
# Declare a sum_of_evens_and_odds function that accepts a tuple of numbers.
# It should return a tuple with two numeric values:
# -- the sum of the even numbers
# -- the sum of the odd numbers.
#
# sum_of_evens_and_odds((1, 2, 3, 4))   => (6, 4)
# sum_of_evens_and_odds((1, 3, 5))      => (0, 9)
# sum_of_evens_and_odds((2, 4, 6))      => (12, 0)

def sum_of_evens_and_odds(tuple_of_numbers):
    sum_of_even = 0
    sum_of_odds = 0
    for number in tuple_of_numbers:
        if number % 2 == 0:
            sum_of_odds += number
        else:
            sum_of_even += number
    return tuple((sum_of_odds, sum_of_even))


def asi_lo_hace_mi_maestro(numbers):

    sum_of_evens = [number for number in numbers if number % 2 != 0]
    sum_of_odds = [number for number in numbers if number % 2 == 0]

    return (sum(sum_of_odds), sum(sum_of_evens))

print(sum_of_evens_and_odds((1, 2, 3, 4)))
print(sum_of_evens_and_odds((1, 3, 5)))
print(sum_of_evens_and_odds((2, 4, 6)))
print() # Elegant Way of Doing the puzzle
print(asi_lo_hace_mi_maestro((1, 2, 3, 4)))
print(asi_lo_hace_mi_maestro((1, 3, 5)))
print(asi_lo_hace_mi_maestro((2, 4, 6)))