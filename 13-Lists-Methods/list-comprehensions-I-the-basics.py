numbers = [2, 3, 5, 7, 2, 1, 8, 9]

# squares = []

# for number in numbers:
#     squares.append(number ** 2)

# print(squares)

squares = [number ** 2 for number in numbers]
print(squares)

rivers = ["Amazon", "Nile", "Usumacinta"]
print([len(river) for river in rivers])

expressions = ["lol", "lmao", "idk"]
print([expression.upper() for expression in expressions])

decimals = [2.32, 4.53, 2.0, 6.54, 3.78]
print([int(decimal) for decimal in decimals])