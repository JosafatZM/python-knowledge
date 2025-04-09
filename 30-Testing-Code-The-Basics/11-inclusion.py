import unittest

class InclusionTests(unittest.TestCase):

    def test_inclusion(self):

        self.assertIn("k", "kangaroo")
        self.assertIn("5", [1, 3, '5'])
        self.assertIn('a', {'a': 3,
                            'b': 7}.keys())
        self.assertIn(7, {'a': 3,
                            'b': 7}.values())
        self.assertIn(9, range(1, 10))

    def test_non_inclusion(self):
        
        self.assertNotIn("a", "Julio")
        self.assertNotIn(7, [1, 2, 3, 4, 5])
        self.assertNotIn('a', {'b':2,
                               'c': 3}.keys())
        self.assertNotIn(1, {'b':2,
                             'c': 3})
        

if __name__ == "__main__":
    unittest.main()