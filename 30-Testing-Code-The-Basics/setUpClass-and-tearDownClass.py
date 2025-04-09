import unittest

class TestOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This will run ONCE before the unit test suite starts")

    def setUp(self) -> None:
        print("This will run before EACH test")
        return super().setUp()
    
    def tearDown(self) -> None:
        print("This will print after EACH test")
        return super().tearDown()

    @classmethod
    def tearDownClass(cls) -> None:
        print("This will run ONCE after the unit test suite finishes")

    def test_stuff(self):
        self.assertEqual(1, 1)

    def test_more_stuff(self):
        self.assertIsInstance(4, int)



if __name__ == "__main__":
    unittest.main()