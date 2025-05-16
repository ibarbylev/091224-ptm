"""Методы множества"""


my_set = {1, 2, 3, 4, 5}

print(""" 1. ====================== remove(value) ====================== """)
print(my_set.remove(5))    # None
print(my_set)              # {1, 2, 3, 4}

try:
    my_set.remove(5)
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")  # KeyError: 5


print(""" 2. ====================== discard(value) ====================== """)
print(my_set)               # {1, 2, 3, 4}
print(my_set.discard(4))    # None
print(my_set)               # {1, 2, 3}

print(my_set.discard(100))  # None
print(my_set)               # {1, 2, 3}


print(""" 3. ====================== pop() ====================== 
(удаление случайного элемента)
""")
print(my_set.pop())         # 1
print(my_set)               # {2, 3}

try:
    my_set.pop(5)
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")  # TypeError: set.pop() takes no arguments (1 given)


print(""" 4. ====================== clear() ====================== """)
print(my_set)               # {2, 3}
print(my_set.clear())       # None
print(my_set)               # set()

