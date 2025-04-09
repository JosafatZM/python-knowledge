from unittest.mock import Mock

# and object that takes the place of other object in a test
pizza = Mock()
print(pizza)
print(type(pizza))

pizza.configure_mock(
    size = "Large",
    price = 19.99,
    toppings = ["pepperoni", "mushroom", "sausage"]
)

# we can se the attributes we just create even
# though they're not defined explicitly in the class
print(pizza.size)

# we can invent instance methods
print(pizza.cover_with_cheese())
# or attributes
print(pizza.anything)