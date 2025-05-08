"""Пример переполнения стека"""


def countdown_recursion(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        return countdown_recursion(n-1)


countdown_recursion(10000)
