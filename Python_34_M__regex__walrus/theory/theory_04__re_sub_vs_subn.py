""" re.sub(<паттерн поиска>, <паттерн замены>, <строка>)"""

import re

pattern = r"(\b\w+)\s\1"
text = "hello hello world world"

result = re.findall(pattern, text)
print(result)  # ['hello', 'world']

""" re.sub заменяет все вхождения шаблона pattern на указанный текст.

В данном случае, каждый раз, когда шаблон находит два повторяющихся слова, 
он заменяет их на первое слово (\1), окруженное ***.

Таким образом, строка "hello hello world world" преобразуется в "hello world".
"""

replaced_text = re.sub(pattern, r"***\1***", text)
print(replaced_text)
# ***hello*** ***world***


# re.subn() - не только находит и заменяет, но и подсчитывает число замен
replaced_text_and_count = re.subn(pattern, r"***\1***", text)
print(replaced_text_and_count)
# ('***hello*** ***world***', 2)


"""Что надо сделать, если мы хотим окружить КАЖДОЕ слово,
причём независимо от регистра.
"""
new_pattern = r"(\b[a-z]+\b)"
new_text = "Hello hello world worLd"
replaced_text = re.sub(new_pattern, r"***\1***", new_text, flags=re.IGNORECASE)
print(replaced_text)
