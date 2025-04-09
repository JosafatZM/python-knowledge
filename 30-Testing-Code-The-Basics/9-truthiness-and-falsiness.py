import unittest

class TrethinessAndFalsinessTestts(unittest.TestCase):

    def test_of_thruetiness(self):
        self.assertTrue(True)
        self.assertTrue("HELLO")
        self.assertTrue({"number": 5})
        self.assertTrue(["3"])
        self.assertTrue(5)
 
    def test_falsiness(self):
        self.assertFalse(False)
        self.assertFalse(0)
        self.assertFalse([])
        self.assertFalse({})
        self.assertFalse("")


if __name__ == "__main__":
    unittest.main()