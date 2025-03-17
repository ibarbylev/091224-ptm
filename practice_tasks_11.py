"""Написать функцию validate_customers(customer), которая принимает на входе список кортежей:
    Имя
    Фамилия
    Дата рождения
    Номер банковского счёта (IBAN)

Функция возвращает словарь, где
    - ключом является строка имя+фамилия,
    - а значением - список сообщений об ошибках, возникших при валидации пользователя по следующим правилам:
        - Имя и фамилия не должны быть пустыми.
        - Возраст валиден, если он больше 18 лет.
        - Ошибки валидации IBAN (см. примечание в конце условий)

IBAN должен соответствовать стандарту длины (начинаться с кода страны и содержать правильное количество символов)
https://en.wikipedia.org/wiki/International_Bank_Account_Number

Решение должно использовать исключения и итераторы.

PS
Параметры IBAN в значительной степени зависят от страны-нахождения банка.
Поэтому для простоты считаем, что все счета - только из Германии.
Например, IBAN: DE89370400440532013000
Проверяем:
 - длина (после удаления внутренних пробелов) - 22 символа
 - первые 2 символа - буквы
 - остальные 20 символов - цифры
"""
from collections import defaultdict
from datetime import datetime
from pprint import pprint

users = [
    ('', 'Doe', '2005-03-28', 'DE44443333222211110000'),  # Пустое имя
    ('John', 'Smith', '2008-10-25', 'XE345678901234567890'),  # Возраст меньше 18 лет
    ('Michael', 'Brown', '1990-05-15', 'DE89370400440532013000'),  # Все данные корректны
    ('Anna', 'Johnson', '1985-12-07', '5511112222333344445555'),  # Первые два символа не буквы
    ('Emily', 'Taylor', '1999-08-03', 'DE9876543210987654321A'),  # Часть из последних 20 символов - не цифры
    ('', 'Taylor', '2020-08-03', '1465DE9876543210987654321A'),  # Все возможные ошибки
    ('Robert', 'Davis', '1992-04-12', 'DE1234567890123456789012')  # Длина IBAN не равна 22 символам
]

# {'Anna_Johnson': ['IBANException: The first two characters must be letters!'],
#  'Emily_Taylor': ['IBANException: The last twenty characters must be digits!'],
#  'John_Smith': ["AgeException: The client's age cannot be less than 18 years!",
#                 'IBANException: Incorrect Length of IBAN!'],
#  'Michael_Brown': [],
#  'Robert_Davis': ['IBANException: Incorrect Length of IBAN!'],
#  '_Doe': ['NameException: Empty name or/and surname'],
#  '_Taylor': ['NameException: Empty name or/and surname',
#              "AgeException: The client's age cannot be less than 18 years!",
#              'IBANException: Incorrect Length of IBAN!; The first two '
#              'characters must be letters!; The last twenty characters must be '
#              'digits!']}


class NameException(Exception):
    pass


class AgeException(Exception):
    pass


class IBANException(Exception):
    pass


def name_validation(name, surname) -> bool:
    """Функция проверяет наличие имени и фамилии

    :param name, surname
    :return: True, если имя и фамилия не пустая строка или None
    :raises NameException: Empty name or/and surname
    """
    if not name or not surname:
        raise NameException("Empty name or/and surname")
    return True


def age_validation(birth_date: str) -> bool:
    """Проверяет, исполнилось ли человеку 18 лет на текущую дату.

    :param birth_date: Дата рождения в формате 'YYYY-MM-DD'.
    :return: True, если возраст 18 лет и более.
    :raises AgeException:  The client's age cannot be less than 18 years!
    """
    if datetime.now().year - int(birth_date.split('-')[0]) < 18:
        raise AgeException("The client's age cannot be less than 18 years!")
    return True


def iban_validation(iban: str) -> bool:
    """Проверяет корректность IBAN.

    :param iban: IBAN (DE).
    :return: True, счёт удовлетворяет всем критериям IBAN.
    :raises IBANException: в комментарии может быть набор из ошибок:
        Incorrect Length of IBAN!
        The first two characters must be letters!
        The last twenty characters must be digits!
    """
    message = []
    if len(iban) != 22:
        message.append("Incorrect Length of IBAN!")
    if iban[:2] != 'DE':
        message.append("The first two characters must be letters!")
    if iban[2:].isdigit():
        message.append("The last twenty characters must be digits!")

    if message:
        raise IBANException(f"{'; '.join(message)}")
    return True


def validate_customers(list_tuples: list[tuple[str, ...]]) -> dict[str, list[str]]:
    """Функция формирует словарь из всех возможных ошибок по каждому клиентов"""
    # ('', 'Doe', '2005-03-28', 'DE44443333222211110000'),

    d = defaultdict(list)
    for client in list_tuples:
        name, surname, date, iban = client
        try:
            name_validation(name, surname)
        except NameException as e:
            d[f"{name}_{surname}"].append(f"{e.__class__.__name__}: {e}")

        try:
            age_validation(date)
        except AgeException as e:
            d[f"{name}_{surname}"].append(f"{e.__class__.__name__}: {e}")

        try:
            iban_validation(iban)
        except IBANException as e:
            d[f"{name}_{surname}"].append(f"{e.__class__.__name__}: {e}")

    return d

def main():
    pprint(validate_customers(users))


if __name__ == '__main__':
    main()
