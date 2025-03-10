"""Необходимо создать функцию get_alphabet_statistics(), которая
 - принимает текст
 - и возвращает словарь в формате: <буква: её количество в этом тексте>

Перед обработкой текста его необходимо перевести в нижний регистр.
"""
from pprint import pprint


def get_alphabet_statistics(text: str) -> dict[str, int]:
    d = {}
    for char in text.lower():
        if char.isalpha():
            d[char] = d.get(char, 0) + 1

    return d


text = 'Winston Churchill: "Those who never change their minds never change anything"'
pprint(get_alphabet_statistics(text))

# {'a': 3,
#  'c': 4,
#  'd': 1,
#  'e': 8,
#  'g': 3,
#  'h': 8,
#  'i': 5,
#  'l': 2,
#  'm': 1,
#  'n': 9,
#  'o': 3,
#  'r': 4,
#  's': 3,
#  't': 4,
#  'u': 1,
#  'v': 2,
#  'w': 2,
#  'y': 1}
