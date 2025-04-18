"""Создать класс животных, имеющий атрибут species,
и далее создать объекты этого класса:
3 вида животных - собака, кошка и лошадь.
(Animal -> dog, cat, horse)
Не забудьте при выводе экземпляра класс на печать отобразить значение его атрибутов.
"""


class Animal:
    pass


dog = Animal('dog')
cat = Animal('cat')
horse = Animal('horse')

print(dog)
print(cat)
print(horse)

# Animal(species=dog)
# Animal(species=cat)
# Animal(species=horse)






""" 02 ========================================================
Создайте класс Car для представления автомобиля.
Класс должен иметь атрибуты brand (марка) и model (модель),
которые передаются в конструкторе при создании экземпляра класса.
Реализуйте метод __str__, который будет возвращать строку
в формате "Марка: <марка>, Модель: <модель>".

Ожидаемый вывод:

Марка: Toyota, Модель: Camry
Марка: BMW, Модель: X5
"""


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Марка: {self.brand}, Модель: {self.model}"


car1 = Car("Toyota", "Camry")
car2 = Car("BMW", "X5")

print(car1)
print(car2)




""" 03 ========================================================
Добавьте счётчик количества выпущенных с конвейера автомобилей count,
который должен увеличиваться на 1
при создании очередного экземпляров класса.
"""




print(f"Всего выпущено автомобилей: {Car.count}")

car1 = Car("Toyota", "Camry")
print(car1)
print(f"Всего выпущено автомобилей: {Car.count}")

car2 = Car("BMW", "X5")
print(car2)
print(f"Всего выпущено автомобилей: {Car.count}")


# 0
# Марка: Toyota, Модель: Camry
# 1
# Марка: BMW, Модель: X5
# 2








""" 04 ======================================================
Создайте класс Circle с конструктором,
который принимает радиус в качестве аргумента.
Включите в класс два метода:
    - get_area() для вычисления площади круга и
    - get_circumference()` для вычисления длины окружности.

Создайте экземпляр класса Circle и вызовите оба метода,
выведя результаты, округленные до 2 знаков после запятой.

Создайте список circles, состоящий из 10 экземпляров класса Circle
со случайным значением радиуса в диапазоне от 10 до 50.

Напишите функцию, которая принимает этот список и
возвращает tuple
    - среднего значения всех площадей и
    - среднего значения длин окружностей
всех объектов списка circles.
(с точностью до двух знаков после запятой)


=====  Пример: =====
Для random.seed(42) средние значения должны составлять

Average Area: 2381.64
Average Circumference: 155.19
"""

import math
import random
from typing import List, Tuple


# ВНИМАНИЕ: если установить метода seed с числовым параметром,
# то все псевдослучайные числа при каждом запуске скрипта будут повторяться
random.seed(42)

class Circle:
    pass

def calculate_averages(circles: List[Circle]) -> Tuple[float, float]:
    pass


random.seed(42)
circles = [Circle(random.randint(10, 50)) for _ in range(10)]


av_area, av_circumference = calculate_averages(circles)
print(f"Average Area: {av_area:.2f}")
print(f"Average Circumference: {av_circumference:.2f}")

# Average Area: 2381.64
# Average Circumference: 155.19
