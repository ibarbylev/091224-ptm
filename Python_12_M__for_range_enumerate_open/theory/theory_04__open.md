# Функция `open()` и методы работы с файлами в Python

Функция `open()` используется для открытия файла и работы с ним. Она возвращает файловый объект, через который можно читать или записывать данные.
## 1. open()

`file = open("example.txt", "r")`  # Открывает файл в режиме чтения

Основные режимы открытия файла:
Режим	Описание
"r"	Чтение (по умолчанию). Ошибка, если файла нет.
"w"	Запись. Создает новый файл или очищает существующий.
"a"	Добавление. Записывает в конец файла.
"x"	Создает новый файл. Ошибка, если уже существует.
"b"	Бинарный режим (например, "rb", "wb").
"t"	Текстовый режим (по умолчанию).
"r+"	Чтение и запись без очистки файла.
"w+"	Чтение и запись с очисткой файла.

## 2. Методы чтения
### read(size=-1)

Считывает весь файл или size байт/символов.
```
file = open("example.txt", "r")
content = file.read()  # Читает весь файл
print(content)
file.close()
```
С size:
```
file = open("example.txt", "r")
print(file.read(5))  # Читает первые 5 символов
file.close()
```

### readline()

Читает одну строку из файла.
```
file = open("example.txt", "r")
print(file.readline())  # Читает первую строку
file.close()
```
Если вызвать несколько раз:
```
file = open("example.txt", "r")
print(file.readline())  # Читает первую строку
print(file.readline())  # Читает вторую строку
file.close()
```

### readlines()

Читает все строки в список.
```
file = open("example.txt", "r")
lines = file.readlines()  # ['Первая строка\n', 'Вторая строка\n']
print(lines)
file.close()
```
Можно читать строки в цикле:
```
file = open("example.txt", "r")
for line in file:
    print(line.strip())  # .strip() удаляет лишние \n
file.close()
```
## 3. Запись в файл
### write()

Записывает строку в файл (без автоматического добавления \n):
```
file = open("example.txt", "w")
file.write("Hello, world!\n")
file.write("Second line")
file.close()

writelines()
```
Записывает список строк:
```
file = open("example.txt", "w")
file.writelines(["First line\n", "Second line\n"])
file.close()
```

### 4. close()

Закрывает файл, освобождая ресурсы.
```
file = open("example.txt", "r")
print(file.read())
file.close()
```
Лучший вариант — `with open()` (автоматически закрывает файл):
```
with open("example.txt", "r") as file:
    print(file.read())  # Файл закроется автоматически после выхода из блока
```
Итог

    read() — читает весь файл или заданное количество символов.
    readline() — читает одну строку.
    readlines() — читает все строки в список.
    write() — записывает строку.
    writelines() — записывает список строк.
    close() — закрывает файл (или используем with open()).

