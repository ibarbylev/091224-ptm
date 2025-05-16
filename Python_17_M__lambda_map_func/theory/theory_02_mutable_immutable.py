"""Что делать, если мы не хотим менять содержимое передаваемых в функцию mutable данных?

Один из вариантов - передавать копии mutable данных
"""


def func(lst, value):
    value += "bc"
    lst[0] = value
    return lst


nums = [1, 2, 3]
latter = 'a'
nums_copy = nums.copy()

func(nums_copy, latter)
print('nums =', nums)
print('latter = ', latter)