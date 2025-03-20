"""Напишите генератор, который принимает в качестве аргумента
генераторной функции generator_unique_elements_from_list(lst) список элементов
и выдает только уникальные элементы, не изменяя их порядок в списке.
Проверьте правильность работы генератора с помощью цикла.

Пример:
lst = [1, 2, 2, 3, 4, 1, 5, 3, 4]
Результат:
1
2
3
4
5"""


def generator_unique_elements_from_list(stream: list):
    pass


input_stream = [1, 2, 2, 3, 4, 1, 5, 3, 4]

for unique in generator_unique_elements_from_list(input_stream):
    print(unique)