import argparse

# Определение ожидаемых результатов:

parser = argparse.ArgumentParser(description='Пример использования argparse')

# Определение аргументов
parser.add_argument('arg1', type=int, help='Положительное целое число')
parser.add_argument('--kwarg1',
                    type=int,
                    choices=range(1, 11),
                    help='Значение позиционного аргумента kwargs1 должно лежать в диапазоне от 1 до 10')

# Разбор аргументов командной строки
args = parser.parse_args()  # Namespace(arg1='1', kwarg1='2')
print(args)

# Вывод переданных аргументов
print('Позиционный аргумент:', args.arg1)
print('Именованный аргумент:', args.kwarg1)

# Вызов скрипта с передачей параметров:
# python theory_05_argparse_check_args_type.py 1 --kwarg1 2
# python theory_05_argparse_check_args_type.py 1 --kwarg1 11
