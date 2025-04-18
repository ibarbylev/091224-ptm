"""Неизменяемые типы данных, которые передаются в функцию, вынуждены создавать свои копии,
чтобы изменяться.
Изменяемые - изменяются сами.
"""


def func(lst, value):
    value += "bc"
    lst[0] = value
    return lst


nums = [1, 2, 3]
latter = 'a'
func(nums, latter)
print('nums =', nums)
print('latter = ', latter)


nums = [1, 2, 3]
latter = 'a'
print('=== Передаём не список nums, а его копию ===')
func(nums.copy(), latter)
print('nums =', nums)
print('latter = ', latter)