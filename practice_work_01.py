"""Реализовать простую поисковую систему.
Для данных в формате surname-name-birth_year-course-points реализовать функцию find_person()
В качестве аргументов это функция будет получать:
    - поле, по которому надо искать,
    - и значение, которое надо найти.
Если есть, то вернуть все подходящие записи,
если нет – вывести сообщение об ошибке.
Задача должна работать максимально быстро, при этом использование памяти не так важно.

Идея решения:
Самый быстры поиск происходит по хэшу.
Следовательно, необходимо создать словарь data с ключами - именами полей.
    data = {
        'surname': {},
        'name': {},
        'birth_year': {},
        'course': {},
        'points': {}
    }

В свою очередь, значение каждого имени поля - тоже словарь, где
    ключ - значение поля конкретного пользователя ('Smith' для surname)
    значение - список из значений списка persons, совпадающий с ключом
                    ["Smith-John-1990-Engineering-85", "Smith-Anna-1993-Python-88"]

    data = {
        'surname': {
            'Smith': ["Smith-John-1990-Engineering-85", "Smith-Anna-1993-Python-88"],
            'Doe': ["Doe-Jane-1992-Python-90"],
            'Brown': ["Brown-Mike-1991-Engineering-75", "Brown-Mary-1990-Python-92"]
        },
        'name': {},
        ...
        'points': {}
    }


Иными словами, создать такой словарь словарей data,
который бы по ключам
        data['surname']['Smith']
давал бы значение
        ["Smith-John-1990-Engineering-85", "Smith-Anna-1993-Python-88"]


"""

persons = [
    "Smith-John-1990-Engineering-85",
    "Doe-Jane-1992-Python-90",
    "Brown-Mike-1991-Engineering-75",
    "Smith-Anna-1993-Python-88",
    "Brown-Mary-1990-Python-92"
]


def create_fields_data(persons):
    """Создаём словарь fields для быстрого поиска данных по ключам"""
    data = {
        'surname': {},
        'name': {},
        'birth_year': {},
        'course': {},
        'points': {}
    }

    pass


def find_person(data, field, value):
    pass

# Индексация данных
data = create_fields_data(persons)

# Примеры поиска
result = find_person(data, 'surname', 'Smith')
print(result)  # ['Smith-John-1990-Engineering-85', 'Smith-Anna-1993-Python-88']

result = find_person(data, 'birth_year', '1990')
print(result)  # ['Smith-John-1990-Engineering-85', 'Brown-Mary-1990-Python-92']

result = find_person(data, 'course', 'C++')
print(result)  # No matching records found

result = find_person(data, 'name', 'John')
print(result)  # ['Smith-John-1990-Engineering-85']
