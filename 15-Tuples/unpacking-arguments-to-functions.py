
def product(a, b):
    
    return a * b

list_numbers = [2, 3]
tuple_numbers = (4, 9)

print(product(*list_numbers))
print(product(*tuple_numbers))

tuple = ("Hi", 3, 2.0, True, [])

*variable_1, v2, v3, v4 = tuple

print(variable_1)
print(v2)
print(v3)
print(v4)