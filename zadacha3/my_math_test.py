import unittest
from my_math import My_math

class TestCubes(unittest.TestCase):

    def test_val(self):
        x = My_math (5,2)
        self.assertEqual(x.a, 5)
        self.assertEqual(x.b, 2)

    def test_operation_sub(self):
        x = My_math(5,2)
        self.assertEqual(x.subtraction(),2)

    def test_operation_add(self):
        x = My_math(5, 2)
        self.assertEqual(x.addition(), 7)

    def test_operation_div(self):
        x = My_math(5, 2)
        self.assertEqual(x.division(), 2.5)

    def test_operation_mul(self):
        x = My_math(5, 2)
        self.assertEqual(x.multiplication(), 10)


    if __name__ == "__main__":
        unittest.main()
