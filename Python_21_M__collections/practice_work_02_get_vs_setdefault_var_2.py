"""Создать функцию get_statistics_by_words, которая
 - принимает текст
 - и возвращает словарь в формате <буква: [её количество в каждом слове, где есть хотя бы одна]>.

Перед начало работы текст необходимо перевести в нижний регистр.
"""
from pprint import pprint

text = 'Bernard Shaw: "Life isn\'t about finding yourself. Life is about creating yourself."'


def get_statistics_by_words(text):
    d = {}
    for word in text.lower().split():
        for char in word:
            if char.isalpha():
                d.setdefault(char, []).append(word.count(char))

    return d


pprint(get_statistics_by_words(text))
