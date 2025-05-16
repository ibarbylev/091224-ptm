"""Функция get_area() рассчитывает площадь квадрата, прямоугольника или прямоугольного треугольника:

Необходимо создать на её основе функции, которые вычисляют площадь только одной фигуры:
    square_area(side1)
    rectangle_area(side1, side2)
    right_triangle_area(side1, side2)
При решении необходимо использовать functools.partial
"""

from functools import partial


def get_area(side1, side2, is_triangle=False):
    if side2 is None:
        side2 = side1
    if is_triangle:
        return side1 * side2 * 0.5
    return side1 * side2


square_area = ...
rectangle_area = ...
right_triangle_area = ...


print(square_area(3))  # 9
print(rectangle_area(2, 3))  # 6
print(right_triangle_area(2, 3))  # 3.0
