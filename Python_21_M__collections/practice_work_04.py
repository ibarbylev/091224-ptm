"""Необходимо создать функцию get_alphabet_statistics, которая
 - принимает текст;
 - и возвращает словарь в формате: <буква: её количество в этом тексте>

Перед обработкой текста его необходимо перевести в нижний регистр.

Задачу необходимо выполнить с помощью collections.Counter
"""
from pprint import pprint

text = ('Mark Twain: "If you don\'t read the newspaper, you\'re uninformed. '
        'If you read the newspaper, you\'re misinformed."')


def get_alphabet_statistics(text: str) -> dict[str, int]:
    from collections import Counter

    list_of_letters = [s for s in text.lower() if s.isalpha()]
    counter_obj = Counter(list_of_letters)
    return dict(counter_obj)


pprint(get_alphabet_statistics(text))
