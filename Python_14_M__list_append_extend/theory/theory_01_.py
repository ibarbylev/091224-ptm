lst = [1, 2, 3]

# ===== append() ========
lst.append(4)
print(lst)   # [1, 2, 3, 4]

lst.append([5])
print(lst)   # [1, 2, 3, 4, [5]]

# ===== extend() ========
lst = [1, 2, 3, 4]
lst.extend([5])
print(lst)  # [1, 2, 3, 4, 5]

lst = [1, 2, 3, 4, 5] + [6]
print(lst)  # [1, 2, 3, 4, 5, 6]
