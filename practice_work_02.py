"""Напишите функцию powerset, которая принимает список и возвращает множество,
содержащее все возможные подмножества этого списка.
Используйте множественные включения для решения этой задачи.

Пример списка
[1, 2, 3]
Пример вывода:
{frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2}), frozenset({3}),
frozenset({1, 3}), frozenset({2, 3}), frozenset({1, 2, 3})}

Описание и примеры функции combinations:
https://docs.python.org/3.12/library/itertools.html#itertools.combinations
"""

from itertools import combinations


print(list(combinations([1, 2, 3], 0)))
print(list(combinations([1, 2, 3], 1)))
print([frozenset(x) for x in combinations([1, 2, 3], 1)])
print(list(combinations([1, 2, 3], 2)))
print(list(combinations([1, 2, 3], 3)))



result = ...

print(result)
