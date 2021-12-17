import unittest
from zadacha1 import Count_elements

class Test_Count_elements(unittest.TestCase):

    def setUp(self) -> None:
        self.num_list = [1, 1, 3, 2, 1, 1, 3, 4]
        self.answer = {
            1: 4,
            3: 2,
            2: 1,
            4: 1
        }

    def test_count_elements(self):
        c = Count_elements(self.num_list)
        self.assertEqual(c.count_elements(), self.answer)

if __name__ == '__main__':
    unittest.main()
