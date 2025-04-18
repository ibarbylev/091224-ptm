set1 = {1, 2, 3}
set2 = {2}
issuperset = set1.issuperset(set2)
issubset = set2.issubset(set1)
print(issuperset)
print(issubset)

print(set1.issuperset(set1) == (set1 >= set2))    # True
print(set2.issubset(set1) == (set2 <= set1))    # True

print(set1 == set2)   # False
print(set1 != set2)   # True
print()

# =============== set equality ===============
print({1, 2, 3} == {3, 1, 2})
print()

# =============== list equality ===============
print([1, 2, 3] == [3, 1, 2])
print([1, 2, 3] == [1, 2, 3])
