"""1. Решите задачу с помощью list comprehension:
Напишите функцию, которая принимает строку от пользователя и разбивает ее на отдельные слова.
Затем программа должна создать список, содержащий длину каждого слова в исходной строке.
"""


def length_of_each_word(text: str) -> list[int]:
    pass


t = "Напишите функцию которая принимает строку от пользователя"
print(length_of_each_word(t))   # [8, 7, 7, 9, 6, 2, 12]


"""2.1. Напишите функцию, которая возвращает True, если текст содержит правильную скобочную последовательность.
И False - если нет.
Вариант для одного вида скобок ().
"""


def is_valid_parentheses(sequence: str) -> bool:
    pass


# Примеры использования
print(is_valid_parentheses("()") == True)      # True
print(is_valid_parentheses("(())") == True)    # True
print(is_valid_parentheses("(()") == False)    # True
print(is_valid_parentheses(")(") == False)     # True
print(is_valid_parentheses("())(") == False)   # True


"""2.2. Напишите функцию, которая возвращает True, если текст содержит правильную скобочную последовательность.
И False - если нет.
Вариант для трёх видов скобок (){}[].
"""


def is_valid_brackets(sequence: str) -> bool:
    pass


print(is_valid_brackets("()") == True)  # True
print(is_valid_brackets("([])") == True)  # True
print(is_valid_brackets("{[()]}") == True)  # True
print(is_valid_brackets("{[(])}") == False)  # False
print(is_valid_brackets("{[}") == False)  # False
print(is_valid_brackets("[({})]") == True)  # True
print(is_valid_brackets("[({})](]") == False)  # False


"""3. Напишите программу, которая принимает список чисел от пользователя и создаёт новый список,
содержащий только положительные числа из исходного списка.
Проверку, является ли каждое значение числом, проводить не нужно.
Используйте списковые включения (list comprehensions) для создания нового списка.

Пример вывода:
Введите список чисел, разделенных пробелами: -2 5 -8 10 -1 0 7
Положительные числа из списка: [5, 10, 7]
"""


def get_positive_numbers(text: str) -> list[int]:
    pass


num_str = "-2 5 -8 10 -1 0 7"
print(get_positive_numbers(num_str))  # [5, 10, 7]
