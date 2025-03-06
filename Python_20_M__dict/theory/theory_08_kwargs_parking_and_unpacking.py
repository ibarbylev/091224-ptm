"""Напишите функцию create_user_profile(), которая принимает обязательные аргументы
first_name и last_name,
а также произвольное количество именованных аргументов для создания профиля пользователя.
Функция должна возвращать словарь, содержащий всю информацию о пользователе.

Пример вызова функции:
    create_user_profile(
        first_name="John",
        last_name="Doe",
        age=30,
        location="New York",
        occupation="Engineer"
    )

Ожидаемый результат:
        first_name: John
        last_name: Doe
        age: 30
        location: New York
        occupation: Engineer
"""
from pprint import pprint


def create_user_profile(first_name, last_name, **kwargs) -> dict[str, str | int]:
    profile_base = {
        first_name: first_name,
        last_name: last_name,
    }

    return profile_base | {k: v for k, v in kwargs.items()}


profile = create_user_profile(
    "John",
    "Doe",
    age=30,
    location="New York",
    occupation="Engineer"
)

pprint(profile)


""" ========================== unpacking ========================= """
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'location': 'New York',
    'occupation': 'Engineer'
}

create_user_profile(**person)
