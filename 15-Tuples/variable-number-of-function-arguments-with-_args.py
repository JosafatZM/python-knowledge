# CASO 1
def my_max(*numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

print(my_max(1, 2, 3, 4, 5, 6))
print(my_max(1, 3, 7, 10, 22, 45, 3, 5, 6, 8, 1))

print()
# CASO 2
def another_max(nonsense, *numbers):
    print(nonsense)
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

print(another_max(1, 2, 3, 4, 5, 6))
print(another_max(1, 3, 7, 10, 22, 45, 3, 5, 6, 8, 1))


# CASO 3
def another_another_max(*numbers, nonsense):
    print(nonsense)
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

print()
# Esto genera un TypeError cause' I'm missing the keyword
# print(another_another_max(1, 2, 3, 4, 5,6))
# print(another_another_max(1, 3, 7, 10, 22, 45, 3, 5, 6, 8, 1))

# Tienes que declarar la keyword de nonsense para que el codigo corra
print(another_another_max(1, 2, 3, 4, nonsense = "Pikachu"))
print(another_another_max(1, 3, 7, 10, 22, 45, 3, 5, 6, 8, nonsense = "Raychu"))




# TONTERIAS XD

# def squares(numbers):
#     squares = [number ** 2 for number in numbers] 
#     return squares

# print(squares([1, 2, 3, 4, 5]))