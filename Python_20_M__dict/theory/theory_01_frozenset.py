"""Неизменяемое множество frozenset() -
это set() в который нельзя добавить или удалить элемент.
"""

print(""" =============== function frozenset() ===============
IMPORTANT: 
    a.) Must have iterable object!!!
    b.) And every item must be hashable!!!!!
""")

f_set = frozenset({1, 2, 3})
print(type(f_set))   # <class 'frozenset'>
print(f_set)         # frozenset({1, 2, 3})

f_set = frozenset([1, 2, 3])
print(type(f_set))   # <class 'frozenset'>
print(f_set)         # frozenset({1, 2, 3})

try:
    frozenset([1, 2, [3]])
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")
