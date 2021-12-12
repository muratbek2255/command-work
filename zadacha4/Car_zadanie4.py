class Car:

    def __init__(self, color='', type1='', year=''):
        self._color = color
        self._type = type1
        self._year = year 


    def car_started(self):
        return 'Автомобиль заведён!'


    def car_muffled(self):
        return 'Автомобиль заглушён!'

    def set_color(self, color):
        self._color = color
        return self._color

    def set_type(self, type1):
        self._type = type1
        return self._type

    def set_year(self, year):
        self._year = year
        return self._year

car1 = Car()
print(car1.car_started())
print(car1.car_muffled())
print('Color : ',car1.set_color("GREEN"))
print('Type  : ',car1.set_type("LEXUS"))
print('Year  : ',car1.set_year(2022))

