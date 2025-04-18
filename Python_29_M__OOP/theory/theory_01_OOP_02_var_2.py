
class Shape:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return 2 * (self.side1 + self.side2)


class Rectangle(Shape):
    """Initialize a Rectangle object with the given side lengths."""


class Square(Shape):
    """Initialize a Square object with the given side length."""

    def __init__(self, side):
        super().__init__(side, side)


class RightTriangle(Shape):
    """Initialize a RightTriangle object with the given leg lengths."""

    def area(self):
        return super().area() / 2

    def perimeter(self):
        hypotenuse = (self.side1 ** 2 + self.side2 ** 2) ** 0.5
        return self.side1 + self.side2 + hypotenuse


rectangle = Rectangle(3, 4)
print(rectangle.__dict__)   # {'side1': 3, 'side2': 4}
print(rectangle.__dir__())  # ['side1', 'side2', '__doc__', 'area', 'perimeter']
print(rectangle.__doc__)    # Initialize a Rectangle object with the given side lengths.

square = Square(3)
print(square.__dict__)   # {'side1': 3, 'side2': 3}
print(square.area())
print(square.perimeter())

rt = RightTriangle(3,4)
print(rt.area())
