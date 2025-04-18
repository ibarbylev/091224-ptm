from typing import Iterator

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get only even items
filer_iter = filter(lambda x: x % 2 == 0, nums)
print(filer_iter)  # <map object at 0x7f7edb9de560>
print("filter - это итератор" if isinstance(filer_iter, Iterator) else "")
print(list(filer_iter))


