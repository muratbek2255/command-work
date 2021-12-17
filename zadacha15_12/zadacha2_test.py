import unittest
from zadacha2 import change_to_star


class MyTestCase(unittest.TestCase):
    def test_something(self):
        c = 'Hellgio World'
        self.assertEqual(change_to_star(c), 'Hello*World')  # add assertion here


if __name__ == '__main__':
    unittest.main()