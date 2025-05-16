from abc import ABC, abstractmethod

# Пример сознательно СОДЕРЖИТ ОШИБКИ!!!

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2


class RightTriangle(Rectangle):
    def area(self):
        return super().area() / 2


r = Rectangle(3, 4)
print(r.area())

rt = RightTriangle(5, 6)
print(rt.area())

