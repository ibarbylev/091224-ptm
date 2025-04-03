"""Предположим, нам необходимо сложить сумму квадратов всех чётных чисел в списке"""

from functools import reduce
from operator import add

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers)))
print(result)
# Результат: 20


sq_nums = ...
even_nums = ...
res = ...
print(res)
