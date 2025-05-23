import unittest

def copy_and_add_element(values, element):
    copy = values[:]
    copy.append(element)
    return(copy)


class TestInequality(unittest.TestCase):

    def test_inequality(self):
        self.assertNotEqual("hello", "Hello")
        self.assertNotEqual(4, "4")

    def test_copy_and_add_element(self):

        values = [1, 2, 3]
        result = copy_and_add_element(values, 4)

        self.assertEqual(result, [1, 2, 3, 4])

        self.assertNotEqual(
            values, 
            [1, 2, 3, 4],
            "The copy_and_add_element function is mutating the input."\
            "make shure that you are creating a copy"
        )

if __name__ == "__main__":
    unittest.main()