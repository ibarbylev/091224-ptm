from typing import Iterator

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Convert int to string
map_iter = map(str, nums)
print(map_iter)  # <map object at 0x7f7edb9de560>
print("map - это итератор" if isinstance(map_iter, Iterator) else "")
print(list(map_iter))


