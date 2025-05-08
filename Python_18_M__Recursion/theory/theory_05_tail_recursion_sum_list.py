"""Sum list

Пример хвостовой рекурсии
"""


def sum_list_tail_recursion(lst, accumulator=0):
    if not lst:
        return accumulator
    return sum_list_tail_recursion(lst[1:], lst[0] + accumulator)


print(sum_list_tail_recursion([1, 2, 3, 4, 5]))  # 15
print(sum_list_tail_recursion([1]))  # 1
print(sum_list_tail_recursion([0]))  # 0
