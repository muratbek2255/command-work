import unittest
from Car_zadanie4 import Car


class TestCar(unittest.TestCase):

    def test_init(self):
        c = Car('black')
        self.assertEqual(c._color, 'black')
        self.assertEqual(c._type,'')
        self.assertEqual(c._year, 10)

    def test_car_started(self):
        c = Car()
        self.assertEqual(c.car_started(),'Автомобиль заведён!')

    def test_car_muffled(self):
        c = Car()
        self.assertEqual(c.car_muffled(),'Автомобиль заглушён!')

    def test_set_color(self):
        c = Car()
        self.assertEqual(c.set_color('White'),'White')

    def test_set_type(self):
        c = Car()
        self.assertEqual(c.set_type('BMW'),'BMW')

    def test_set_year(self):
        c = Car()
        self.assertEqual(c.set_year(2021),2021)


    if __name__ == "__main__":
        unittest.main()





