animals = ["elephant", "horse", "cat", "giraffe", "cheetah", "dog"]

length_of_animals = [animal for animal in animals if len(animal) > 5]
print(length_of_animals)

def is_long_animal(animal):
    return len(animal) > 5

print()
print(list(filter(is_long_animal, animals)))
print()
print(is_long_animal(animals))
# help(filter)