"""set comprehension позволяет создать множество на основе итерируемого объекта.
Главное условие: элементы нового множества должны быть immutable!!!
(Как правило, immutable означает hashable. Но есть исключения!)
"""

new_set = {x for x in range(5)}
print(type(new_set))   # <class 'frozenset'>
print(new_set)         # {0, 1, 2, 3, 4}


"""Попытка создать новый сет на основе изменяемых (mutable) элементов приведёт к ошибке:"""

try:
    new_set_2 = {[x] for x in range(5)}
except Exception as e:
    print(f"ERROR!!! {e.__class__.__name__}: {e}")     # TypeError: unhashable type: 'list'

