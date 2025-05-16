from functools import reduce
from typing import Iterator

nums = [1, 2, 3, 4, 5, 6, 7, 8]

""" =========================== map =========================== """
map_object = map(str, nums)
print(map_object)
print(isinstance(map_object, Iterator))
print(*map_object)
print()

map_object_2 = map(lambda x, y: x + y, nums, nums)
print(*map_object_2)
print()

""" =========================== map =========================== """
filter_obj = filter(lambda x: x % 2 == 0, nums)
print(filter_obj)
print(isinstance(filter_obj, Iterator))
print(*filter_obj)
print()

""" =========================== reduce =========================== 
reduce(function, sequence[, initial])
    function — функция, принимающая два аргумента (аккумулятор и текущий элемент).
    iterable — последовательность элементов.
    initial (необязательный) — начальное значение аккумулятора.
По умолчанию initial равен отсутствию значения.
Если initial не указан, он становится равным первому элементу.
После этого reduce() начинает применять функцию, начиная со второго элемента.
(сделайте CTRL + клик по функции reduce и посмотрите код самой reduce)
"""

reduce_obj = reduce(lambda acc, x: acc + x, nums, 10)
print(reduce_obj)  # 46
reduce_obj2 = reduce(lambda acc, x: acc + x, [10, 0, 0])
print(reduce_obj2)  # 10
