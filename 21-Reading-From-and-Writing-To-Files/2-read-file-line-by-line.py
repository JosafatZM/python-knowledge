# This is how you read a file line by line

# Sin saltos de linea
with open("cupcakes.txt", "r") as cupcake_file:
    for line in cupcake_file:
        print(line.strip())

# Space
print()

# Con saltos de linea
with open("cupcakes.txt") as file:
    for line in file:
        print(line)
