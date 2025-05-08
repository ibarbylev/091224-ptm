def all_more_than_value(nums: list[int | float], value: int | float):
    """Все ли без исключения элементы списка больше value?"""
    return all(n > value for n in nums)


def at_least_one_is_bigger(nums: list[int | float], value: int | float):
    """Хотя бы один элемент больше value?"""
    return any(n > value for n in nums)


lst = [2, 9, 4, 1, 12]
print(all_more_than_value(lst, 0))
print(at_least_one_is_bigger(lst, 11))
