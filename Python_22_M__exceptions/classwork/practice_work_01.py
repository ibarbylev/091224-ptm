"""Напишите программу, которая будет считывать данные из файла names.txt
и будет формировать список кортежей из пяти полей:
    фамилия, имя, год рождения, курс и баллы.
Обработайте следующие ошибки:
    файла не существует,
    нельзя считать из файла,
    число элементов в стоке не равно 5!
    год рождения, курс и/или баллы не являются числом,
    и т.п. и т.д.

Пример входного файла:
Ivanov		Ivan		1980		2	80
Smith		Ann		    2000		1	67
Petrov		Petro		1999		1	90	43
Schmidt	    Marta		1976		3
Johnson	    John		1965g		5	99
Archer		Leonard		1978		v5	51

ВНИМАНИЕ!!!
Есть готовые исключения.
Необходимо написать программу и правильно разместить эти исключения в коде.
"""


class IncorrectNumberOfElements(Exception):
    pass


try:
    with open('../names.txt', encoding='utf-8') as file:
        for line in file:
            pass




except IncorrectNumberOfElements as e:
    print(f'{e.__class__.__name__} {e}')
except ValueError as e:
    print(f'Год рождения, курс и/или баллы не являются числом в строке: {line.strip()}'
          f'\n{e.__class__.__name__} {e}')

except FileNotFoundError as e:
    print(f'Файла не существует: {e.__class__.__name__} {e}')
except (IOError, OSError, UnicodeDecodeError) as e:
    print(f'Нельзя считать данные из файла: {e.__class__.__name__} {e}')
except Exception as e:
    print(f'{e.__class__.__name__} {e}')

