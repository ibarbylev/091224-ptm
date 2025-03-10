"""Имеется множество уникальных слов set_uniq_words = {"cat", "dog", "animals"}
Необходимо написать функцию add_info, которая добавляет в него новые уникальные слова из текста,
переданного в неё в качества аргумента и возвращает это изменённое множество.

Известно, что текст не содержит знаков препинания и букв в верхнем регистре.
"""

set_uniq_words = {"cat", "dog", "animals"}


def add_uniq_info(text: str, set_uniq_words: set[str]) -> set[str]:
    pass


words = "my dog is my best friend"
print(add_uniq_info(words, set_uniq_words))
# {'dog', 'is', 'my', 'animals', 'friend', 'best', 'cat'}
