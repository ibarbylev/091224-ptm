"""Сравнение скорости поиска элементов в list и set"""

from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        print(f"{50 * '='}\nStart func {func.__name__} ...")
        func(*args, **kwargs)
        end = time()
        print(f"Func {func.__name__} execution time: {end - start:.2f}")
    return wrapper


@timer
def find_item_in_list(value, lst, num):
    for _ in range(num):
        if value in lst:
            pass


@timer
def find_item_in_set(value, sset, num):
    for _ in range(num):
        if value in sset:
            pass


value = -1
num = 20000
lst = ['a' * n for n in range(num)]    # ['a', 'aa', 'aaa', ...]
sset = set(lst)

find_item_in_list(value, lst, num)
find_item_in_set(value, sset, num)
