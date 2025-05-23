"""
This is a Docstring
A regular python string that creates technical
documemtation for a piece of your program
"""

import sushi

help(sushi)

print("\n ----- ejercicio ----- \n")
# Define a CollegeStudent class that accepts and assigns a university attribute.

# Add a docstring for the class equal to "Blueprint for a student at an institution of higher learning"

# Define three instance methods — sleep, eat, and party. 
# The actual content of the methods is irrelevant (feel free to use the pass keyword)

# The sleep method should have the docstring "Sleep through class".
# The eat method should have the docstring "Go to the cafeteria".
# The party method should have the docstring "Hit the books hard".

# To simplify the test evaluation, submit ALL docstrings without any line breaks.
# Example: """Sample docstring"""
# You're welcome to use single quotes, double quotes, or triple quotes.

# See sample execution below

class CollegeStudent():
    """Blueprint for a student at an institution of higher learning"""

    def __init__(self,university) -> None:
        self.university = university
        
    def sleep():
        """Sleep through class"""
        pass

    def eat():
        """Go to the cafeteria"""
        pass

    def party():
        """"Hit the books hard"""
        pass




print(CollegeStudent.__doc__) # Blueprint for a student at an institution of higher learning

marty = CollegeStudent("Python Community College") 
print(marty.sleep.__doc__) # Sleep through class
print(marty.eat.__doc__)   # Go to the cafeteria
print(marty.party.__doc__) # Hit the books hard