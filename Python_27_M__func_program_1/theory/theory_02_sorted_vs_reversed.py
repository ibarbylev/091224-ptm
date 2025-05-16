from typing import Iterator, Iterable

nums = [1, 5, 3, 4, 2]

sorted_nums = sorted(nums)
print(sorted_nums)   # [1, 2, 3, 4, 5]

print(isinstance(sorted_nums, list))
print(isinstance(sorted_nums, Iterable))
print(isinstance(sorted_nums, Iterator))

print(' ============== reversed =============== ')
reversed_nums = reversed(nums)
print(reversed_nums)   # <list_reverseiterator object at 0x7fb9515da770

print(isinstance(reversed_nums, list))
print(isinstance(reversed_nums, Iterable))
print(isinstance(reversed_nums, Iterator))
