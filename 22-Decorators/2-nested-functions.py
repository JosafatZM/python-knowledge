# Gallons to cups 

# 1 gallon = 4 quarts
# 1 quart = 2 pints 
# 1 pint = 2 cups

def gallon_to_cups(gallons):

    def gallon_to_quarts(gallons):
        return gallons * 4

    def quarts_to_pints(quarts):
        return quarts * 2

    def pint_to_cups(pints):
        return pints * 2

    quarts = gallon_to_quarts(gallons)
    pints = quarts_to_pints(quarts)
    cups = pint_to_cups(pints)

    return f"{gallons} gallon = {cups} cup"

print(gallon_to_cups(1))