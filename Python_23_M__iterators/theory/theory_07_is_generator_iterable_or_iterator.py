from typing import Iterator, Iterable, Generator


g = (x for x in range(3))

print(isinstance(g, Iterable))
print(isinstance(g, Iterator))
print(isinstance(g, Generator))


"""Генераторы в Python являются частным случаем итераторов, 
потому что они не только реализуют все методы итератора, 
но и предоставляют удобный синтаксис для создания итераторов 
с использованием ключевого слова yield. 
Таким образом, каждый генератор является итератором, 
но не каждый итератор является генератором.
"""

# it = [1, 2, 3].__iter__()
#
# print(isinstance(it, Iterable))
# print(isinstance(it, Iterator))
# print(isinstance(it, Generator))
