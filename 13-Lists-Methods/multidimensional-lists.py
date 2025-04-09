bubble_tea_flavors = [
    ["Honeydew", "Mango", "Passion Fruit"],
    ["Peach", "Plum", "Strawberry", "Taro"],
    ["Kiwi", "Chocolate"]
]

print(len(bubble_tea_flavors))
print(bubble_tea_flavors[0])
print(bubble_tea_flavors[1])
print(bubble_tea_flavors[-1])

print(bubble_tea_flavors[0][1])
print(bubble_tea_flavors[1][2])
print(bubble_tea_flavors[2][0])

#Colocar a todos en una sola lista y no en una matriz
print()

flavors_list = []

for flavors in bubble_tea_flavors:
    for flavor in flavors:
        flavors_list.append(flavor)

print(flavors_list)


print("\n**** Ejercicio ****\n")
# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# EXAMPLES
# nested_sum([[1, 2, 3], [4, 5]])            => 15
# nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
# nested_sum([[]])                           => 0

def nested_sum(nested_lists):
    sum = 0

    for lists in nested_lists:
        if len(lists) == 0:
            continue
        for value in lists:
            sum += value
    return sum

print(nested_sum([[1, 2, 3], [4, 5]]))
print(nested_sum([[1, 2, 3], [], [], [4], [5]]))
print(nested_sum([[]]))            

print("\n**** Ejercicio ****")
# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3
#
# EXAMPLES
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]])                 => ""

def fancy_concatenate(nested_lists):

    concatenated_list = ""

    for lists in nested_lists:
        if len(lists) == 3:
            concatenated_list += "".join(lists)
        else:
            continue
    return concatenated_list

print(fancy_concatenate([["A", "B", "C"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]]))
print(fancy_concatenate([["A", "B"], ["C", "D"]]))
print(fancy_concatenate([["A", "B", "C"], ["D", "E"]]))

# Another way of doing it is not as fancy as mine

def another_fancy_concatenate(lists):

    final = ""

    for row in lists:
        if len(row) == 3:
            for string in row:
                final += string
    
    return final 