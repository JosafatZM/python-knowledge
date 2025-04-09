class NegativeNumbersError(Exception):
    """One or more inputs are negative"""
    pass

def add_positive_numbers(a, b):

    try:
        if a <= 0 or b <=0:
            raise NegativeNumbersError
        
    except NegativeNumbersError as e:
        return f"Shame on you, not valid!: {e}"
    
print(add_positive_numbers(-4, 3))