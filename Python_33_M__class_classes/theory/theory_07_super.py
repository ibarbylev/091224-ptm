"""Из класса Shape наследуем класс Square (квадрат)
и класс RightTriangle (прямоугольный треугольник),
используя функцию super()
"""


class Shape:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        return self.side1 * self.side2

    def __str__(self):
        attrs = ', '.join(f'{k}={v}' for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"


class Square(Shape):

    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.side1})"


class RightTriangle(Shape):

    def get_area(self):
        return super().get_area() // 2


sq = Square(4)
print(sq)
print(sq.get_area())

rt = RightTriangle(4, 4)
print(rt)
print(rt.get_area())

# Square(side=4)
# 16
# RightTriangle(side1=4, side2=4)
# 8