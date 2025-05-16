"""iterable vs iterator"""

from typing import Iterator, Iterable
from sys import getsizeof as size

lst = [1, 2, 3, 4, 5, 6, 7]

print(isinstance(lst, Iterable))  # True
print(isinstance(lst, Iterator))  # False

print("""1. К итерируемому объекту можно применить iter() или __iter__()""")

lst_iterator = lst.__iter__()

print(isinstance(lst_iterator, Iterable))  # True
print(isinstance(lst_iterator, Iterator))  # True

print("""2. Но ТОЛЬКО к итератору можно применить next() или __next__()""")

try:
    next(lst)
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")  # TypeError: 'list' object is not an iterator


print(next(lst_iterator))
print(next(lst_iterator))
print(next(lst_iterator))
print(next(lst_iterator))
print(next(lst_iterator))
print(next(lst_iterator))
print(next(lst_iterator))


try:
    print(next(lst_iterator))
except StopIteration as e:
    print(f"{e.__class__.__name__}: {e}")  # StopIteration:

"""ВЫВОД: итератор может исчерпать все свои значения"""

print("""3. Отсюда: операция in работает для итератора ТОЛЬКО ОДИН РАЗ!!!""")

lst_iterator = lst.__iter__()
print('3 in lst_iterator', 3 in lst_iterator)  # True
print('3 in lst_iterator', 3 in lst_iterator)  # False


print("""4. Что требует бОльшей памяти: iterator или iterable?""")

print(size(lst))   # 120
print(size(lst_iterator))  # 48

"""ВЫВОД: По сути, iterator можно считать "ленивой" версией iterable-объекта:
элементы там не хранятся в полном объёме, а "выдаются" только в момент обращения
к итератору с помощью next() или __next___()
"""