"""Словарь синонимов.
Вам дан словарь, состоящий из пар слов.
Каждое слово является синонимом к парному ему слову.
Все слова в словаре различны.
Написать функцию, которая для заданного слова из словаря, определяет его синоним.

Пример словаря:
    dct = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}

    get_synonym(“Goodbye”) -> Bye.
    get_synonym(“Plate) -> THe word <Plate> was not found in the dictionary!
"""


def get_synonym(synonyms: dict, word: str) -> str:
    pass


words = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}

print(get_synonym(words, "Goodbye"))  # Bye
print(get_synonym(words, "List"))     # Array
print(get_synonym(words, "Plate"))    # Word <Plate> was not found in the dictionary!


""" 02 ===========================================================================

Дан json-файл 'cities-countries.json', в котором
по ключу <Страна> находится строка с названиями городов, разделённых пробелом.

Напишите функцию, которая:
 - считывает данные из файла;
 - по аргументу ГОРОД возвращает
    - либо название страны
    - либо "not found"

which_country("Novgorod") = Russia
which_country("Mumbai") = Not found

"""
import json


def read_json_file(filename: str) -> dict[str, str]:
    pass


def which_country(city: str) -> str:
    pass


print(which_country("Novgorod"))   # Russia
print(which_country("Turin"))      # Italy
print(which_country("Mumbai"))     # Not found


""" 03 ==========================================================================="""

"""Дана база данных о продажах некоторого интернет-магазина.
Каждая строка файла 'sales.json' представляет собой запись вида
покупатель-товар-количество, где
    покупатель — имя покупателя (строка без пробелов),
    товар — название товара (строка без пробелов),
    количество — количество приобретенных единиц товара.

Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных
им единиц каждого вида товаров.
Список покупателей, а также список товаров для каждого покупателя
нужно выводить в лексикографическом порядке.

Данные:
[
    "Alice-apple-5",
    "Alice-orange-3",
    "Bob-apple-2",
    "Bob-banana-7",
    "Alice-banana-2",
    "Charlie-apple-1
]

Пример вывода:
    {'Alice': {'apple': 5, 'banana': 2, 'orange': 3},
     'Bob': {'apple': 2, 'banana': 7},
     'Charlie': {'apple': 1}}
"""
import json
from pprint import pprint


def read_list_from_json_file(filename: str) -> dict[str, str]:
    pass


def process_sales_data(filename: str) -> dict[str, dict[str, int]]:
    pass


sales_dict = process_sales_data('sales.json')
pprint(sales_dict)

# {'Alice': {'apple': 5, 'banana': 2, 'orange': 3},
#  'Bob': {'apple': 2, 'banana': 7},
#  'Charlie': {'apple': 1}}


""" 04 ==========================================================================="""

"""Дополните условие предыдущей задачи:
Информацию о продажах необходимо вывести в файл 'sales-by-customers.json'
"""
import json
from pprint import pprint


def read_list_from_json_file(filename: str) -> dict[str, str]:
    pass


def write_list_from_json_file(filename: str, dct: dict[str, dict[str, int]]) -> None:
    pass


def process_sales_data(read_from_file: str, write_to_file: str) -> None:
    pass


process_sales_data('sales.json', 'sales-by-customers.json')


""" 05 ==========================================================================="""

"""Добавьте к условиям задачи 1 возможность добавления пользователем собственных синонимов."""
synonyms = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}


