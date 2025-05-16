""" Вычисление суммы списка
Sum list
"""


def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])


print(sum_list([1, 2, 3, 4, 5]))  # 15
print(sum_list([1]))  # 1
print(sum_list([0]))  # 0


""" Кстати, это пример НЕ хвостовой рекурсии: 
вызов рекурсии не является последней операцией в функции, 
так как рекурсивная функция суммируется с lst[0]:

    return lst[0] + factorial_loop(n-1)
"""