import unittest
from unittest.mock import MagicMock

class BurritoBowl():
    restaurant_name = "Bobo's Restaurant"

    @classmethod
    def steak_special(cls):
        return cls("Steak", "White", 1)
    
    def __init__(self, protein, rice, guacamole_portions):
        self.protein = protein
        self.rice = rice
        self.guacamole_portions = guacamole_portions

    def add_guac(self):
        self.guacamole_portions += 1


class_mock = MagicMock(spec = BurritoBowl)
print(class_mock.restaurant_name)
print(class_mock.steak_special())


instace_mock = MagicMock(spec_set = BurritoBowl.steak_special())
print(instace_mock.protein)
print(instace_mock.rice)
print(instace_mock.guacamole_portions)
print(instace_mock.add_guac())
