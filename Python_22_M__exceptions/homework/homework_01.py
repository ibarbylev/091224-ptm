"""Напишите программу, которая
 - открывает файл,
 - считывает из него два числа
 - и выполняет операцию их деления.

Если число отрицательное, выбросите исключение
ValueError с сообщением "Число должно быть положительным".

Обработайте исключение и выведите соответствующее сообщение.
"""

try:

    with open('file_1.txt', encoding='utf-8') as file:
        x_str, y_str = file.read().split()
        x, y = float(x_str), float(y_str)

        if x < 0 or y < 0:
            raise ValueError("Число должно быть положительным")

        print(x / y)


except ValueError as e:
    print(f"{e.__class__.__name__}: {e}")
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")

