chinese_food = {
    "Pollo agridulce":[1, 2],
    "Costillas BBQ": [1, 2],
    "Fideos": [1, 2],
    "Arroz": [1, 2]
}

for food in chinese_food:
    print(f"The food is {food} and it's price is {chinese_food[food][1]}")


print(f"The food is {chinese_food['Arroz']} and it's price is {chinese_food[food][1]}")
# Anti-Pattern: 
# A solution to a programming problem that is considered ineffective
# ot counter-productive 
print()

pound_to_kilograms = {
    5: 2.26796,
    10: 4.53592,
    20: 11.3398
}

for pound in pound_to_kilograms:
    print(f"{pound} pounds is equal to {pound_to_kilograms[pound]} kilograms. ")