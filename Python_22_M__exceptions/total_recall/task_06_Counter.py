"""Функция принимает текст и возвращает словарь, где
    ключи - символы, из которых состоит тест,
    значения - их количество.

Решите задачу с помощью collections.Counter

Пример:
get_statistics("Python is the best!")

# {'P': 1, 'y': 1, 't': 3, 'h': 2, 'o': 1, 'n': 1, ' ': 3, 'i': 1, 's': 2, 'e': 2, 'b': 1, '!': 1}
"""

from collections import Counter


def get_statistics(text: str) -> dict:
    return ...


txt = "Python is the best!"
print(get_statistics(txt))
