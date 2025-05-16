"""Функция accumulate позволяет накапливать значение в каждом элементы.
Возвращает итератор
"""
import functools
import itertools
import operator

numbers = [1, 2, 3, 4, 5]
iter_accumulate = itertools.accumulate(numbers, operator.mul)
print(iter_accumulate)   # <itertools.accumulate object at 0x7f380d3a49a0>
print(*iter_accumulate)  # 1 2 6 24 120


reduce_acc = functools.reduce(operator.mul, numbers)
print(reduce_acc)