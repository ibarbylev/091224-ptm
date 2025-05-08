"""Выполнить сериализацию / десериализацию объекта:
person = {"name": "John", "age": 25}

Убедиться в том, словари до преобразования идентичен словарю после.
"""

person_source = {"name": "John", "age": 25}
print(type(person_source))  # dict

person_source_str = ...
print(type(person_source_str))  # str

person_destination = ...
print(type(person_destination))  # dict

print(person_source == person_destination)
