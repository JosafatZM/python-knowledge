# Dunder methods

# Hook: a procedure that intercepts
# a process at some point in its
# execution 

# everything in python is an object 
# so everything has methods

"""
MAGIC METHODS
They can be used to make our custom objects play
friendly with existing Python functionalities like
iteration, indexing, length, truthiness and more.
"""

print(3.3 + 4.4)
# what happens behid the escenes
print(3.3.__add__(4.4))

print(len([1, 2, 3, 4, 5]))
# magic method 
print([1, 2, 3, 4, 5].__len__())

print("h" in "hello")
# magic method
print("hello".__contains__("h"))

print(["a", "b", "c"][2])
# magic method
print(["a", "b", "c"].__getitem__(2))