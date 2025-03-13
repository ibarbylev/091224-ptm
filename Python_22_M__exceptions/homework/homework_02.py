"""Напишите программу, которая
 - открывает файл,
 - считывает его содержимое
 - и выполняет операции над числами в файле.

Обработайте возможные исключения
 - при открытии файла (FileNotFoundError)
 - и при выполнении операций над числами (ValueError, ZeroDivisionError).

Используйте конструкцию try-except-finally для обработки исключений
и закрытия файла в блоке finally.
"""

try:
    with open('file_1.txt', encoding='utf-8') as file:
        x_str, y_str = file.read().split()
        x, y = float(x_str), float(y_str)
        if x < 0 or y < 0:
            raise ValueError("Число должно быть положительным")

        print(x / y)

except FileNotFoundError as e:
    print(f"{e.__class__.__name__}: {e}")
except ValueError as e:
    print(f"{e.__class__.__name__}: {e}")
except ZeroDivisionError as e:
    print(f"{e.__class__.__name__}: {e}")
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")