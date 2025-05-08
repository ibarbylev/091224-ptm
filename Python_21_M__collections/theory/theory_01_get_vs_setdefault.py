"""Различие между методами .get() и .setdefault()

Метод my_dict.get(key, value)
 - если ключ key существует
        возвращает my_dict[key];
 - если ключ key НЕ существует
        возвращает value (None по умолчанию).

Метод my_dict.setdefault(key, value)
 - если ключ key существует
        возвращает my_dict[key];
 - если ключ key НЕ существует
        создаёт my_dict[key] = value
        возвращает my_dict[key]
"""

my_dict = {'name': 'John'}
print('my_dict =', my_dict)

print('\n ==== Method .get() ===')
x = my_dict.get('surname', 'Smith')
print('x =', x)
print('my_dict =', my_dict)

print('\n ==== Method .setdefault() ===')
x = my_dict.setdefault('surname', 'Smith')
print('x =', x)
print('my_dict =', my_dict)
