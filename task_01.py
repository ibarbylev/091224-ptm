"""Создайте бесконечный генератор square_generator(), который принимает целое число и возвращает его квадрат.
"""


def square_generator():
    pass


gen = square_generator()
# Инициализация генератора
next(gen)

print(gen.send(3))  # 9
print(gen.send(4))  # 16
print(gen.send(5))  # 25

