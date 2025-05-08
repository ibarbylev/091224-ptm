from functools import partial
from typing import Callable


# Создание новой функции, которая всегда будет использовать аргумент x = 2
multiply_by_two = partial(lambda x, y: x * y, 2)

print(isinstance(multiply_by_two, Callable))
result = multiply_by_two(5)
print(result)  # Выводит 10
