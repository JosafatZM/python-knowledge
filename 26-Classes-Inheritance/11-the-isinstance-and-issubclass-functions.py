print(type({}))

print(isinstance({}, dict))
print(isinstance({}, int))

print(isinstance([], (list, dict, int)))
print(isinstance(3.4, (list, dict, int)))

print("\n")

class Person():
    pass

class SuperHero(Person):
    pass

Josa = SuperHero()
Juan = Person()

# # TypeError: issubclass() arg 1 must be a class
# print(issubclass(Josa, SuperHero))

print(issubclass(SuperHero, Person))
print(issubclass(Person, SuperHero))
print(issubclass(SuperHero, object))

