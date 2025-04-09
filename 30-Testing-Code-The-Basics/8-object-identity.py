import unittest

class IdentityTest(unittest.TestCase):

    def test_identicaly(self):
        a = [1, 2, 3]
        b = a 
        c = [1, 2, 3]

        self.assertEqual(a, b)
        self.assertEqual(a, c)

        self.assertIs(a, b)
        self.assertIsNot(a, c)
        self.assertIsNot(c, b)

if __name__ == "__main__":
    unittest.main()