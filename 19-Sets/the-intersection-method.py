# This method returns the elements that are repeated in both sets
# Such as the ones I'm currently proving it with 

code_languages = {"Python", "R", "Ruby", "Java"}
favorite_letters = {"R", "J", "X", "B"}

print(code_languages.intersection(favorite_letters))
# anther syntax
print(code_languages & favorite_letters)

# Espacio 1
print()

values = {3.0, 4.0, 5.0}
more_values = {3, 5, 3, 6}

print(values.intersection(more_values))
print(more_values.intersection(values))
print(more_values & values)
print(values & more_values)