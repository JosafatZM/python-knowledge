mr_freeze = frozenset([1, 2, 3])
print(mr_freeze)

# I can pass it a a key on a dictionary cause'
# it is an unmutable object

# Example 

# I couldn´t do this whit a regular set cause' it's mutable
print({ mr_freeze: "Some value" })