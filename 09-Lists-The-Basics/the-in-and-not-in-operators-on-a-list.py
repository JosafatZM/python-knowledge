meals = ["breakfast", "lunch", "dinner"]

print("lunch" in meals)
print("dessert" in meals)
print("desssert" not in meals)

test_scores = [99.0, 78.3, 87.7]

print()
print(99 in test_scores)
print(99.0 in test_scores)
print(28 in test_scores)
print(99 not in test_scores)

if 1000 not in test_scores:
    print("THAST RIGTH THE VALUE IS NOT IN THERE")

print()
# Comprobaciones

tricky_list = [5, 4, 3]

print([5, 4, 3] not in tricky_list) # por que es un vector completo 