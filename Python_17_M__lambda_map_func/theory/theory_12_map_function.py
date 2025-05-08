"""Функция map() — это встроенная функция в Python,
которая применяется к каждому элементу последовательности (списка, тюпла и т. д.),
выполняя переданную ей функцию, и возвращает итератор с результатами.

map(func, iterable)
    - iterable - итерируемая последовательность (list, tuple)
    - func - функция, которая будет применена к каждому элементу iterable
"""


def to_upper(s):
    return s.upper()


words = ["hello", "world"]
upper_words = map(to_upper, words)
print(list(upper_words))  # ['HELLO', 'WORLD']
