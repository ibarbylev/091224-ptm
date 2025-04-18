
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    """Initialize a Rectangle object with the given side lengths."""
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return 2 * (self.side1 + self.side2)


class Square(Shape):
    """Initialize a Square object with the given side length."""
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class RightTriangle(Shape):
    """Initialize a RightTriangle object with the given leg lengths."""
    def __init__(self, side1, side2, hypotenuse=None):
        self.side1 = side1
        self.side2 = side2
        self.hypotenuse = hypotenuse if hypotenuse is not None else (side1 ** 2 + side2 ** 2) ** 0.5

    def area(self):
        return (self.side1 * self.side2) / 2

    def perimeter(self):
        return self.side1 + self.side2 + self.hypotenuse


r1 = Rectangle(3, 4)
print(r1.__dict__)   # {'side1': 3, 'side2': 4}
print(r1.__dir__())  # ['side1', 'side2', '__doc__', 'area', 'perimeter']
print(r1.__doc__)


""" ====================== ПОЛИМОРФИЗМ (УНИФИКАЦИЯ) ======================= """


def print_shape_info(shape: Shape):
    print(f"===== {shape.__class__.__name__} =====")
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


shapes = [
    Rectangle(3, 4),
    Square(5),
    RightTriangle(3, 4, 5),
]

for shape in shapes:
    print_shape_info(shape)

