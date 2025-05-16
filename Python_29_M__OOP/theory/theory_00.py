class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


square = Square(3)
print(square.side)
print(square.area())
print(square.perimeter())
