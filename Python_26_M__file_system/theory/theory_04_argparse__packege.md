`argparse` — это стандартный модуль Python для обработки аргументов командной строки. Он позволяет удобно определять, разбирать и использовать аргументы, передаваемые скрипту.
## Основные возможности argparse

- Определение аргументов и их типов.
- Автоматическая генерация справки (--help).
- Возможность задавать значения по умолчанию.
- Поддержка флагов (--option).
- Группировка аргументов.

### Обязательный (позиционный) аргумент

*Создадим скрипт, который принимает один обязательный аргумент (name) и выводит приветствие*:
```
import argparse

parser = argparse.ArgumentParser(description="Программа приветствия")
parser.add_argument("name", type=str, help="Ваше имя")  # Обязательный аргумент

args = parser.parse_args()
print(f"Привет, {args.name}!")
```
Запуск:
```shell
python script.py Иван
```
Вывод:
```
Привет, Иван!
```
### Опциональные (именованные) аргументы (флаги)

*Добавим опциональный аргумент `--age` (допустим также короткий вариант `-age`):*
```
import argparse

parser = argparse.ArgumentParser(description="Программа приветствия")
parser.add_argument("name", type=str, help="Ваше имя")
parser.add_argument("--age", type=int, help="Ваш возраст", default=18)  # Необязательный аргумент

args = parser.parse_args()
print(f"Привет, {args.name}! Тебе {args.age} лет.")
```
Запуск:
```shell
python script.py Иван --age 25
```

Вывод:
```
Привет, Иван! Тебе 25 лет.
```

Если `--age` не указан, будет использовано значение по умолчанию (18).


### Флаги без значений (булевы аргументы)

`action="store_true"` — если аргумент передан, argparse автоматически установит его значение в True;  
 если аргумент отсутствует, значение будет False.


Флаг `--verbose`, который просто включает подробный режим:
(**Подробный режим (verbose mode)** — это режим работы программы, при котором выводится дополнительная информация о выполняемых процессах. Обычно его включают для диагностики или отладки.)
```
import argparse

parser = argparse.ArgumentParser(description="Пример с флагом")
parser.add_argument("--verbose", action="store_true", help="Вывести подробную информацию")

args = parser.parse_args()

if args.verbose:
    print("Подробный режим включен")
else:
    print("Обычный режим")
```
Запуск:

python script.py --verbose

Вывод:
```
Подробный режим включен
```
### Несколько значений в одном аргументе

Если нужно передать несколько значений, используем nargs="+":
```
import argparse

parser = argparse.ArgumentParser(description="Список чисел")
parser.add_argument("numbers", type=int, nargs="+", help="Введите числа через пробел")

args = parser.parse_args()
print(f"Вы ввели числа: {args.numbers}")
```
Запуск:
```shell
python script.py 1 2 3 4 5
```

Вывод:
```
Вы ввели числа: [1, 2, 3, 4, 5]
```

### Выбор значений (choices)

Можно ограничить выбор допустимых значений:
```
import argparse

parser = argparse.ArgumentParser(description="Выбор цвета")
parser.add_argument("color", choices=["красный", "синий", "зелёный"], help="Выберите цвет")

args = parser.parse_args()
print(f"Вы выбрали цвет: {args.color}")
```
Запуск:
```shell
python script.py красный
```
Вывод:
```
Вы выбрали цвет: красный
```
Если передать недопустимое значение:
```
python script.py желтый
```
argparse выдаст ошибку:
```
usage: script.py [-h] {красный,синий,зелёный}
script.py: error: argument color: invalid choice: 'желтый' (choose from 'красный', 'синий', 'зелёный')
```

### Группировка аргументов

Если аргументы логически связаны, их можно сгруппировать:
```
import argparse

parser = argparse.ArgumentParser(description="Настройки пользователя")

group = parser.add_mutually_exclusive_group()  # Создаём взаимоисключающую группу
group.add_argument("--enable-feature", action="store_true", help="Включить функцию")
group.add_argument("--disable-feature", action="store_true", help="Выключить функцию")

args = parser.parse_args()

if args.enable_feature:
    print("Функция включена")
elif args.disable_feature:
    print("Функция выключена")
else:
    print("Функция осталась без изменений")
```
Запуск:
```
python script.py --enable-feature
```
Вывод:
```
Функция включена
```
Если попробовать передать оба аргумента (`--enable-feature` и `--disable-feature`), `argparse` выдаст ошибку.


### Автогенерация справки

При передаче -h или --help выводится справка:
```
 python theory_06_argparse_practice.py -h
```
Пример вывода:
```
usage: theory_06_argparse_practice.py [-h] [--input INPUT] [--output OUTPUT]

options:
  -h, --help       show this help message and exit
  --input INPUT    Path to input file
  --output OUTPUT  Path to output file

```
### Заключение

**argparse** — мощный инструмент для обработки аргументов командной строки. Он автоматически создает справку, обрабатывает ошибки ввода и предоставляет гибкие возможности работы с аргументами.
