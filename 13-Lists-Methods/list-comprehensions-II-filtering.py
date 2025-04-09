print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "donut"])
print([number / 2 for number in range(1,21)]) # rango de 1 a 20, el 21 se excluye

donuts = [
    "Boston Cream",
    "Chocolate Cream",
    "Brownie",
    "Jelly",
    "Glazed",
    "Vanilla Cream"
]

# Creat a list with just the creamy donuts
print([creamy for creamy in donuts if "Cream" in creamy])

# Una lista que me dice la longitud del string de las donas que tienen crema
print([len(donut) for donut in donuts if "Cream" in donut])

# Solo el nombre de la dona cremosa sin el "Cream"
Donut_without_cream_on_its_name_xd = [donut.split(" ")[0] for donut in donuts if "Cream" in donut]
print(Donut_without_cream_on_its_name_xd)


print("\n **** Ejercicio ****\n")
# Uncomment the commented lines of code below and complete the list comprehension logic

# The floats variable should store the floating point values 
# for each string in the values list.
values = ["3.14", "9.99", "567.324", "5.678"]
floats = [float(number) for number in values]
print(floats)

# The letters variable should store a list of 5 strings. 
# Each of the strings should be a character from name concatenated together 3 times.
# i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
name = "Boris"
letters = [name[name.index(char)] * 3 for char in name]
print(letters)

# MANERA ELGANGTE DE PROGRAMAR
print([char * 3 for char in name])

# The 'lengths' list should store a list with the lengths
# of each string in the 'elements' list
elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
lengths = [len(string) for string in elements]
print(lengths)

print("\n **** Ejercicio ****\n")
# Declare a destroy_elements function that accepts two lists.
# It should return a list of all elements from the first list that are NOT contained in the second list.
# Use list comprehension in your solution.
#
# EXAMPLES
# destroy_elements([1, 2, 3], [1, 2])      => [3]
# destroy_elements([1, 2, 3], [1, 2, 3])   => []
# destroy_elements([1, 2, 3], [4, 5])      => [1, 2, 3]

def destroy_elements(list_1, list_2):

    final_list = [number for number in list_1 if number not in list_2]

    return final_list

print(destroy_elements([1, 2, 3], [1, 2]))
print(destroy_elements([1, 2, 3], [1, 2, 3]))
print(destroy_elements([1, 2, 3], [4, 5]))