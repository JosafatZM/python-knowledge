"""
A module related to the joy of sushi.
No fishy code found here!
"""

def fish():
    """
    Determines if fish is a good mela choice.
    Always returns True, because it always is.
    """
    return True

class Salmon():
    """
    Blueprint for a salmon object
    """

    def __init__(self) -> None:
        self.tastiness = 10

    def bake(self):
        """
        Bake the fish in an oven.
        """
        self.tastiness += 1