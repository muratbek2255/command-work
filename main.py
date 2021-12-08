class Soda:
    def __init__(self, dabavka='Обычная'):
        self.drink = "Газировка"
        self.dabavka = dabavka

    def show_my_drink(self):
        return f'{self.drink} and {self.dabavka}'

soda = Soda("Cola")
print(soda.show_my_drink())