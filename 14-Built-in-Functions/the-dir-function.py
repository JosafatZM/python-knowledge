#
print(dir("pasta"))

print(len("pasta"))
print("pasta".__len__())

print("st" in "pasta")
print("pasta".__contains__("st"))

print("Josa" + " ponte verga")
print("pasta".__add__(" and meat balls"))

print()

# HOMEWORK SOLUTION 
values = [3.45, 5.67, 7.89]
# List comprenhension
print([format(value ** 2, ".2f") for value in values])
# "map" function 
def squares(numbers):
    return format(numbers ** 2, ".2f")

print(list(map(squares, values)))

# You can also 
print(list(map(lambda value: format(value ** 2, ".2f"), values)))

