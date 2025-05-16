"""Словарь - упорядоченная коллекция пар "ключ: значение".
Ключом могут быть только хэшируемые (неизменяемые) объекты.
Каждый ключ в словаре - уникален.
Значения могут любыми типами данных.
"""

my_dict = {"name": "John", "age": 25, "city": "New York"}
print(type(my_dict))   # <class 'dict'>
print(my_dict)         # {'name': 'John', 'age': 25, 'city': 'New York'}


print(""" 1. ================== {key: value} =================== """)
d = {1: 1, 2: 2}

try:
    d_mutable_key = {[1]: [2]}
    print(d_mutable_key)
except Exception as e:
    print(f"ERROR!!! {e.__class__.__name__}: {e}")    # TypeError: unhashable type: 'list'


print(""" 2. ================== function dict() =================== """)
empty_dict_1 = {}
print(empty_dict_1)   # {}

empty_dict_2 = dict()
print(empty_dict_2)   # {}

two_dimensional_array = [("name", ["John"]), ("age", 15), ("age", 25), ("city", "New York")]
print(two_dimensional_array)
dict_3 = dict(two_dimensional_array)
print(dict_3)       # {'name': 'John', 'age': 25, 'city': 'New York'}

two_dimensional_array = [(["name"], "John"), ("age", 15), ("age", 25), ("city", "New York")]
print(two_dimensional_array)
try:
    dict_3 = dict(two_dimensional_array)
except Exception as e:
    print(f"ERROR!!! {e.__class__.__name__}: {e}")    # TypeError: unhashable type: 'list'


print(""" 3. ================== dict comprehension =================== """)
dict_comp = {k: v for k, v in enumerate(range(5))}
print(dict_comp)    # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}


print(""" 4. ================== dict.fromkeys() =================== """)

print(dict.fromkeys([1, 2, 3]))   # {1: None, 2: None, 3: None}
print(dict.fromkeys([1, 2, 3], 0))   # {1: 0, 2: 0, 3: 0}
print(dict.fromkeys([1, 2, 3], []))  # {1: [], 2: [], 3: []}
