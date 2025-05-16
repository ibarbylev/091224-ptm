"""Для того чтобы вернулась функция, а не значение None,
необходимо использовать специальную конструкцию,
называемую "замыканием" - "closure".
"""
from typing import Callable


def multiplier_factory(factor):
    def multiplier(x):
        return factor * x
    return multiplier


# Создание замыкания
double = multiplier_factory(2)
triple = multiplier_factory(3)

# Вызов функции
print(double(5))  # 10
print(triple(5))  # 15

print(isinstance(double, Callable))  # True
