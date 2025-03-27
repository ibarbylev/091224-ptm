"""Создайте файл test.py со следующим содержимым:

import sys

print('Список параметров, переданных скрипту')
print(sys.argv)

print([arg for arg in sys.argv if arg[0]!='-'])

Запустите файл test.py следующим образом:

$ python theory_03_little_practise.py -file test.txt -pi 3.14

Попробуйте объяснить, что произошло.
"""

import sys

print('Список параметров, переданных скрипту')
print(sys.argv)

print([arg for arg in sys.argv if arg[0] != '-'])

