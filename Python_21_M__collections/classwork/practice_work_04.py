"""Необходимо создать функцию get_alphabet_statistics, которая
 - принимает текст;
 - и возвращает словарь в формате: <буква: её количество в этом тексте>

Перед обработкой текста его необходимо перевести в нижний регистр.

Задачу необходимо выполнить с помощью collections.Counter
"""
from pprint import pprint
from collections import Counter


def get_alphabet_statistics(text: str) -> dict[str, int]:
    pass


some_text = ('Mark Twain: "If you don\'t read the newspaper, you\'re uninformed. '
             'If you read the newspaper, you\'re misinformed."')

pprint(get_alphabet_statistics(some_text))

# {'a': 6,
#  'd': 5,
#  'e': 12,
#  'f': 4,
#  'h': 2,
#  'i': 6,
#  'k': 1,
#  'm': 4,
#  'n': 7,
#  'o': 7,
#  'p': 4,
#  'r': 9,
#  's': 3,
#  't': 4,
#  'u': 5,
#  'w': 3,
#  'y': 4}
