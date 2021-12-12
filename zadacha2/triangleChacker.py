class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a 
        self.b = b 
        self.c = c 

    def is_triangle(self):

        if isinstance(self.a, str) or isinstance(self.b, str) and isinstance(self.c, str):
            return 'Введены не числа'
        elif self.a < 0 or self.b < 0 or self.c < 0:
            return 'Нельзя построть треугольник с негативными числами!'
        elif self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return 'Ура! Треугольник можно построить!'
        else:
            return 'Нельзя построть треугольник с этими сторонами!'


triangle_parametry = TriangleChecker(16,21,34)
print(triangle_parametry.is_triangle())
