"""Создать функцию get_total_statistics, которая
 - принимает текст
 - и возвращает словарь в формате <буква: её количество в тексте>.

Перед начало работы текст необходимо перевести в нижний регистр.
"""
from pprint import pprint

text = 'Bernard Shaw: "Life isn\'t about finding yourself. Life is about creating yourself."'


def get_total_statistics(text):
    d = {}
    for char in text.lower():
        if char.isalpha():
            d[char] = d.get(char, 0) + 1
    return d


pprint(get_total_statistics(text))
