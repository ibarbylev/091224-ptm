"""Метод setdefault позволяет получить значение по указанному ключу.
Удобен, когда нужно работать со словарями и избегать лишних проверок через if key in dict.
Если ключ отсутствует, он добавляет его со значением по умолчанию и возвращает это значение.

Синтаксис:
dict.setdefault(key, default_value)
    key — ключ, который ищем в словаре.
    default_value — значение, которое будет добавлено, если ключ отсутствует (по умолчанию None).
"""

# 1: Ключ уже есть в словаре

data = {"age": 25}
value = data.setdefault("age", 30)
print(data)  # {'age': 25}
print(value)  # 25

# 2: Ключа ещё нет

value_2 = data.setdefault("weight", 82)  # Добавит ключ "age" со значением 30
print(data)  # {'age': 25, 'weight': 82}
print(value_2)  # 82 (новое значение)

# 3: Список по дефолту

students = {}
students.setdefault("fruit", []).append("apple")
print(students)  # {'fruit': ['apple']}
students.setdefault("fruit", []).append("tomato")
print(students)  # {'fruit': ['apple', 'tomato']}

