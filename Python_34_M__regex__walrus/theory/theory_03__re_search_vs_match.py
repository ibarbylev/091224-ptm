import re

TEXT = """111 22 33-aad 232-15-11 ff 15 
15 555-22-78 223/99-37 223/25/987 123-35 26 258-85-45 
"""

pattern = r'\d{3} \d{2} \d{2}|\d{3}-\d{2}-\d{2}|\d{3}\/\d{2}\/\d{2}'

""" re.search - если находит совпадение, возвращает полную информацию
Если не находит - возвращает None
"""

match = re.search(pattern, TEXT)
print(match.group())  # 111 22 33

match = re.search(r'asdfasdfasdf', TEXT)
print(match)  # None


""" re.match - проверка СТРОГО с начала строки
Если находит совпадение, возвращает полную информацию
Если не находит - возвращает None
"""

match = re.match(pattern, TEXT.lstrip())
print(match.group())  # 111 22 33


# Сдвигаем строку на пробел и получаем ошибку,
# так как совпадения, начиная с начала строки, больше нет
match = re.match(pattern, '  ' + TEXT)
print(match)  # None
