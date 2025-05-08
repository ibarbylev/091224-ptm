"""Дан список овощей и фруктов
items = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape", "Kiwi", "Lemon"]
Необходимо поместить его в хэш таблицу, имитирующую объект set
"""


def _hash(value: str) -> int:
    """Функция для вычисления индекса с помощью hash()"""
    return hash(value) % hash_table_size


def add_item(value):
    idx = _hash(value)

    if hash_table[idx] is None:
        hash_table[idx] = [value]
    else:
        if value not in hash_table[idx]:
            hash_table[idx].append(value)


def is_item_in_set(value):
    idx = _hash(value)

    if hash_table[idx] is None:
        return False
    else:
        return value in hash_table[idx]


def print_table(lst):
    print("Index | Items")
    print("------+----------------------")
    for i, value in enumerate(lst):
        print(f"{i:<5} | {value}")
    print("------+----------------------")
    print()


items = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape", "Kiwi", "Lemon"]

# Определяем размер и создаём по нему хэш таблицу
hash_table_size = len(items)
hash_table: list[None | list[str]] = [None] * hash_table_size
# [None, None, None, None, None, None, None, None]
print_table(hash_table)

for item in items:
    add_item(item)

print_table(hash_table)
