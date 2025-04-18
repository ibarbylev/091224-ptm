"""Методы (и способы), удаляющие элементы из списка)"""

lst = [1, 2, 5, 4, 5]


""" 1. ====================== method remove(value) ======================
Removes the first occurrence of the specified element.
Returns nothing!!!
"""
print(lst.remove(5))  # None    Returns nothing!!!
print(lst)   # [1, 2, 4, 5]

try:
    lst.remove(6)
    print(lst)
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")  # ValueError: list.remove(x): x not in list


""" 2. ====================== method pop() ======================
Removes the last element.
Returns the removed element!!!
"""

print(lst.pop())  # 5   Returns the removed element!!!
print(lst)   # [1, 2, 4]


""" 3. ====================== method pop(index) ======================
Removes the element at the specified index.
"""
lst.pop(1)
print(lst)   # [1, 4]

try:
    lst.pop(10)
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")   # IndexError: pop index out of range


""" 4. ====================== operator del ======================
Removes the element(s) at the specified index.
"""

lst = [1, 2, 3, 4, 5]
del lst[4]
print(lst)   # [1, 2, 3, 4]

del lst[1:3]
print(lst)   # [1, 4]

del lst
try:
    print(lst)
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")   # NameError: name 'lst' is not defined


""" 5. ====================== list comprehension ======================
Creates a new list using the specified parameters
"""
lst = list(range(10))
print(lst)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print([x for x in lst if x % 2 == 0])  # [0, 2, 4, 6, 8]


""" 6. ====================== method clear() ====================== """
print(lst)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst.clear()
print(lst)   # []
