lst = [1, 2, 3, 3]

""" ============== method insert() ============== """
lst.insert(3, 4)
print(lst)  # [1, 2, 3, 4, 3]

""" ============== method remove(value) ============== """
lst.remove(3)
print(lst)  # [1, 2, 4, 3]

# IMPORTANT!!! remove() raises exception, if the item doesn't exist!!!

# lst.remove(5)  # ValueError: list.remove(x): x not in list

value = 5
if value in lst:
    lst.remove(value)

""" ============== method index() ============== """
print(lst.index(3))  # 2

# IMPORTANT!!! index() raises exception, if the item doesn't exist!!!

# print(lst.index(5))  # ValueError: 5 is not in list

value = 5
if value in lst:
    print(lst.index(5))

# method count()
print(lst.count(3))  # 1
print(lst.count(5))  # 0


""" ============== method clear() ============== """
print(lst)   # [1, 2, 4, 3]
lst.clear()

print(lst)   # []


""" ============== operator del ============== """
lst = [1, 2, 3, 3]
print(lst)   # [1, 2, 3, 3]

# del by index
del lst[2]
print(lst)   # [1, 2, 3]

# del by slicing
del lst[1:]
print(lst)   # [1]

# full (complete) deletion of the object
del lst
try:
    print(lst)
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")  # NameError: name 'lst' is not defined
