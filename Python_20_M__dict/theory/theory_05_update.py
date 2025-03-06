"""Добавление в словарь последовательности пар key: value с помощью метода .update()"""
from pprint import pprint

my_dict = {'name': 'John', 'age': 25}
print(f"my_dict = {my_dict}")

print(""" 1. =============== .update(lst) ================ 
где lst = последовательность пар (key, value)
""")

lst = [('city', 'New York'), ('tel', '111-222-33333')]
print(f"lst = {lst}")

my_dict.update(lst)
print(f"my_dict = {my_dict}")
# {'name': 'John', 'age': 25, 'city': 'New York', 'tel': '111-222-33333'}


print(""" 
2. =============== .update(dict) ================ 
где dict - частный случай последовательности пар (key, value), то есть другой словарь
""")

dict_additional = {
    'location': 'London',
    'occupation': 'Engineer'
}

my_dict.update(dict_additional)
pprint(my_dict)

# {'age': 25,
#  'city': 'New York',
#  'location': 'New York',
#  'name': 'John',
#  'occupation': 'Engineer',
#  'tel': '111-222-33333'
#  }


print(""" 
3. =============== concatenation by | ================ 
Начиная с вервии 3.9, словари можно объединять логическим сложением
с помощью оператора |
""")
new_dict = {1: 1} | {2: 2}
print(new_dict)
