The_Simpsons = ["Homero", "Marge", "Bart", "Lisa", "Maggie"]

for word in The_Simpsons[::-1]:
    print(f"{word} has a total of {len(word)} characters.")

print()
print(reversed(The_Simpsons))
print(type(reversed(The_Simpsons)))

print()
for word in reversed(The_Simpsons):
    print(f"{word} has a total of {len(word)} characters.")