import unittest

class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])

    def test_count(self):
        self.assertEqual("josafat".count("a"), 2)


if __name__ == "__main__":
    unittest.main()