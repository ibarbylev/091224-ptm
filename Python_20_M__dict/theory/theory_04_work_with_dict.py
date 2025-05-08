"""Работа со словарями"""

my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

""" 1. ================== get value by [key] =================== """
name = my_dict['name']
print(name)  # John

try:
    address = my_dict['address']
except Exception as e:
    print(f"ERROR!!! {e.__class__.__name__}: {e}")  # ERROR!!! KeyError: 'address'


""" 2. ================== if key in dict =================== """
if 'tel' in my_dict:
    print(my_dict['tel'])


""" 3. ================== get value by method .get(key) =================== """
address = my_dict.get('height')
print(address)    # None


""" 4. ================== change value =================== """
my_dict['age'] = 35
print(my_dict)
# {'name': 'John', 'age': 35, 'city': 'New York', 'height': 182}


""" 5. ================== add new item =================== """
my_dict['weight'] = 82
print(my_dict)
# {'name': 'John', 'age': 35, 'city': 'New York', 'height': 182, 'weight': 82}


""" 6. ================== del (key: value) =================== """
del my_dict['weight']
print(my_dict)
# {'name': 'John', 'age': 35, 'city': 'New York', 'height': 182}


""" 7. ================== pop(key) =================== """
my_dict.pop('height')
print(my_dict)
# {'name': 'John', 'age': 35, 'city': 'New York'}


""" 8. ================== .items() =================== 
Метод возвращает коллекцию тюплов пар (key: value)
"""

print(my_dict.items())   # dict_items([('name', 'John'), ('age', 25), ('city', 'New York')])

for k, v in my_dict.items():
    print(f"{k}: {v}")

# name: John
# age: 25
# city: New York


""" 9. ================== .keys() =================== 
Метод возвращает коллекцию ключей
"""
print(my_dict.keys())   # dict_keys(['name', 'age', 'city'])

# либо просто с помощью list()
print(list(my_dict))   # ['name', 'age', 'city']


""" 10. ================== .values() =================== 
Метод возвращает коллекцию значений
"""
print(my_dict.values())   # dict_values(['John', 25, 'New York'])
