import unittest
from zadacha3 import get_extention


class Extensions (unittest.TestCase):
    def setUp(self) -> None:
        self.succesful_data = ["da.docx", "df.txt", "dj.csv"]
        self.succesful = ['docx', 'txt', 'csv']
        self.wrong_data = ["da.docx", "df", "dj1.csv"]

    def test_succesful(self):
        self.assertEqual(get_extention(self.succesful_data), self.succesful)
    def test_wrong(self):
        with self.assertRaises(EOFError) as context:
            get_extention(self.wrong_data)

if __name__ == '__main__':
    unittest.main()