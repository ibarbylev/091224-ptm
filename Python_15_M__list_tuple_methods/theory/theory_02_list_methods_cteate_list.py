"""Методы (и способы) создания списка"""


""" 1. =============== square brackets [] =============== """
lst = [1, 2, 3]


""" 2. =============== function list() =============== 
IMPORTANT: Must have iterable object!!!
"""

try:
    list(1)
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")


print(list())
print(list(""))
print(list("a"))
print(list("abc"))
print()


""" 3. =============== list comprehension =============== """
print([i for i in range(10)])
print([0 for _ in range(10)])
print()


""" 4. =============== multiplication ( * ) =============== """
print([0] * 10)
