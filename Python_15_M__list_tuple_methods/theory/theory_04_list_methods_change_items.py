"""Методы (и способы), изменяющие элементы в списке (не меняя общее число элементов)"""

lst = [1, 2, 3]


""" 1. =============== insert by index in [] =============== """
lst[0] = 'A'
print(lst)  # ['A', 2, 3]

lst[1:] = ['B', 'C']
print(lst)  # ['A', 'B', 'C']


""" 2. =============== list comprehension =============== """
new_lst = [i+1 for i in range(len(lst))]
print(new_lst)  # [1, 2, 3]


""" 3. =============== function map() =============== """
print(new_lst)
print('l c', [float(i) for i in new_lst])

new_lst = map(float, new_lst)
print(new_lst)   # <map object at 0x7f92476995a0>

new_lst = list(new_lst)
print(new_lst)  # ['1', '2', '3']
