import unittest

class ObjectTypeTest(unittest.TestCase):

    def test_is_instance(self):
        self.assertIsInstance(1, int)
        self.assertIsInstance(1.54, float)
        self.assertIsInstance({}, dict)
        self.assertIsInstance([], list)

    def test_not_is_instance(self):
        self.assertNotIsInstance(1, dict)
        self.assertNotIsInstance("hola", float)
        self.assertNotIsInstance("hola", set)


if __name__ == "__main__":
    unittest.main()