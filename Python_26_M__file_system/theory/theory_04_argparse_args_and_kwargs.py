import argparse

# Создание объекта parser:
parser = argparse.ArgumentParser(description='Пример использования argparse')

# Определение/добавление аргументов
parser.add_argument('arg1', help='Описание позиционного аргумента')
parser.add_argument('--kwarg1', help='Описание именованного аргумента')

# Разбор аргументов командной строки
args = parser.parse_args()  # Namespace(arg1='1', kwarg1='2')
print(args)

# Вывод переданных аргументов
print('Позиционный аргумент:', args.arg1)
print('Именованный аргумент:', args.kwarg1)

# Генерация справки и использование по умолчанию:
# python theory_04_argparse_args_and_kwargs.py --help

# Вызов скрипта с передачей параметров:
# python theory_04_argparse_args_and_kwargs.py 1 --kwarg1 2
