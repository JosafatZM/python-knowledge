from typing import ValuesView


print(not True)
print(not False)

if "H" in "Hello":
    print("Yes it is")

if "Z" not in "Hello":
    print("This will NOT print")

value = 99

if value > 100:
    print("This will not print either")

if value < 100:
    print("Yes it is")

if not value > 100:
    print("Si, el valor no es mayor a 100")