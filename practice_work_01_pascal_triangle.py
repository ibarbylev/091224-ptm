
"""Выведите на экран треугольник Паскаля для некоторого N тем же способом,
что на прошлом уроке записывали его в файл.
a. Решите эту же задачу, используя списки для хранения строк треугольника Паскаля.
b. С помощью %%timeit сравните время выполнения этих алгоритмов.

f(n) // (f(k) * f(n - k))
"""
from math import factorial as f


def binomial_coefficient(n, k):
    return f(n) // (f(k) * f(n - k))


def pascal_triangle(num_rows):
    for i in range(num_rows + 1):
        pass
        
    print("Треугольник Паскаля записан в файл 'pascal_triangle.txt'.")


num = 20
pascal_triangle(num)
