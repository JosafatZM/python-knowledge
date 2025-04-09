import unittest

class Addres():
    def __init__(self, state, city):
        self.state = state
        self.city = city

class Owner():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Restaurant():

    def __init__(self, owner, address):
        self.owner = owner
        self.address = address

    @property
    def owner_age(self):
        return self.owner.age
    
    def summary(self):
        return f"This restaurant is owned by {self.owner.name} and is located in {self.address.city}"
    
class TestRestaurant(unittest.TestCase):

    def setUp(self) -> None:
        print("This will print before each test!")
        address = Addres(city="Guadalajara", state="Jalisco")
        owner = Owner(name="Josafat", age=21)
        self.golden_palace = Restaurant(owner, address)

        return super().setUp()
    
    def tearDown(self) -> None:
        print("This will print after each test!")

        return super().tearDown()
    
    def test_summary(self):
        self.assertEqual(self.golden_palace.summary(),
                         "This restaurant is owned by Josafat and is located in Guadalajara")
    

if __name__ == "__main__":
    unittest.main()

