""" ======================= AREA ============================== """
from collections import namedtuple


def rectangle_area(side1, side2):
    """Calculate the area of a rectangle"""
    return side1 * side2


def square_area(side1):
    """Calculate the area of a square"""
    return side1 ** 2


def right_triangle_area(side1, side2):
    """Calculate the area of a right triangle"""
    return (side1 * side2) / 2


""" ======================= PERIMETR ============================ """


def rectangle_perimeter(side1, side2):
    """Calculate the perimeter of a rectangle"""
    return 2 * (side1 + side2)


def square_perimeter(side1):
    """Calculate the perimeter of a rectangle"""
    return 4 * side1


def right_triangle_perimeter(side1, side2):
    """Calculate the perimeter of a right triangle"""
    hypotenuse = (side1 ** 2 + side2 ** 2) ** 0.5
    return side1 + side2 + hypotenuse


""" ======================= FIGURES ============================ """

# ===============  variant 1 =============

Shape = namedtuple('Shape',
                   ["side1", "side2", "area", "perimeter"])

rectangle_3_4 = Shape(3, 4, rectangle_area, rectangle_perimeter)
print(rectangle_3_4.area(3, 4))
print(rectangle_3_4.perimeter(3, 4))


# ===============  variant 2 =============

rectangle_2 = {
    "side1": 3,
    "side2": 4,
    "area": rectangle_area,
    "perimeter": rectangle_perimeter,
}
