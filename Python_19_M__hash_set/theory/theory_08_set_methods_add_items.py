"""Методы множества"""


my_set = {1, 2, 3}

""" 1. ====================== add(value) ====================== """
print(my_set.add(4))    # None
print(my_set)           # {1, 2, 3, 4}


""" 2. ====================== update(iterable) ====================== """
print(my_set.update([5, 6, 7]))   # None
print(my_set)                     # {1, 2, 3, 4, 5, 6, 7}

print(my_set.update("abc"))      # None
print(my_set)                    # {1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c'}


""" 3. ========= concatenation by | ======== """
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)   # {1, 2, 3, 4, 5}


""" 4. ========= concatenation by .union() ======== """
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))    # {1, 2, 3, 4, 5}



