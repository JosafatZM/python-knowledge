import unittest

def explicit_return_sum(a, b):
    return a + b

def null_return_sum(a, b):
    print(a + b)

class TestNone(unittest.TestCase):

    def test_sum_functions(self):

        self.assertIsNone(null_return_sum(1, 3))
        self.assertIsNotNone(explicit_return_sum(1, 2))

if __name__ == "__main__":
    unittest.main()