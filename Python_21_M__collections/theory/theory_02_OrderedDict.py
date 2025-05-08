"""OrderedDict (упорядоченный словарь) поддерживает все методы обычного словаря,
так как является его подклассом.

Но дополнительно:
1.) Идеально поддерживает порядок сортировки
(обычный словарь даёт сбой при более сложных сортировках)

2.) Работает чуть медленнее обычного (из-за более строго отслеживания порядка)

3.) Содержит 2 полезных метода:
    - move_to_end(key, last=True) – перемещает элемент в конец (last=True)
                                    или в начало (last=False).
    - popitem(last=True) – удаляет и возвращает последний (last=True)
                                    или первый (last=False) элемент.
"""

from collections import OrderedDict


ordered_dict = OrderedDict()
ordered_dict["apple"] = 5
ordered_dict["banana"] = 2
ordered_dict["orange"] = 8

print(ordered_dict)  # OrderedDict({'apple': 5, 'banana': 2, 'orange': 8})

ordered_dict.pop("banana")
print(ordered_dict)  # OrderedDict({'apple': 5, 'orange': 8})

ordered_dict["banana"] = 2
print(ordered_dict)  # OrderedDict({'apple': 5, 'orange': 8, 'banana': 2})


print(""" ============ Сравнение с обычным словарём ============ """)

usual_dict = {}
usual_dict["apple"] = 5
usual_dict["banana"] = 2
usual_dict["orange"] = 8

print(usual_dict)  # {'apple': 5, 'banana': 2, 'orange': 8}

usual_dict.pop("banana")
print(usual_dict)  # {'apple': 5, 'orange': 8}

usual_dict["banana"] = 2
print(usual_dict)  # {'apple': 5, 'orange': 8, 'banana': 2}

