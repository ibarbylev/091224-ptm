"""
Строки - неизменяемы.
Если изменить строковый объект, он будет сохранён по новому адресу.
"""

text = "Hello"
print(id(text), text)
text = text.lower()
print(id(text), text)

