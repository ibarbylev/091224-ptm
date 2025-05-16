"""Рекурсивные функции
"""

import os


def process_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            # Обработка файла
            print(file_path)
        elif os.path.isdir(file_path):
            # Рекурсивный вызов для вложенного каталога
            process_directory(file_path)


start_directory = os.path.abspath('..')
print('start_directory', start_directory)
process_directory(start_directory)
