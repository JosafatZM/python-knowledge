"""
An assertion is an statement that we make that validates
that something evaluates to true
"""

def add(x, y):
    assert isinstance(x, int) and isinstance(y, int), "Both must be integers"
    return x + y


print(add(3, 4))  # Esto funcionará correctamente
print(add(3, "4"))  # Esto generará un AssertionError
