# Методы форматирование вывода `ljust()`, `rjust()` и `center()` 

Используются для выравнивания строк до заданной ширины, заполняя пустое пространство указанным символом.

| Метод                                          | Описание                                      | Пример (`"Hi".method(7, "-")`) |
|------------------------------------------------|--------------------------------|----------------|
| [`ljust(w, c)`](#выравнивание-влево-ljust)     | Выравнивает строку **влево**, заполняя `c` справа | `"Hi-----"` |
| [`rjust(w, c)`](#выравнивание-вправо-rjust)    | Выравнивает строку **вправо**, заполняя `c` слева | `"-----Hi"` |
| [`center(w, c)`](#центрирование-строки-center) | Центрирует строку, заполняя `c` с обеих сторон | `"--Hi---"` |

## Dыравнивание влево ljust
`str.ljust(width, fillchar=' ')`

### Синтаксис:

`string.ljust(width, fillchar=' ')`

    `width` – итоговая длина строки.
    `fillchar` (необязательно) – символ заполнения (по умолчанию пробел).

### Пример:
```
text = "Hello"
print(text.ljust(10, "-"))  # "Hello-----"
```

## Выравнивание вправо rjust
`str.rjust(width, fillchar=' ')`

### Синтаксис:

string.rjust(width, fillchar=' ')

### Пример:
```
print(text.rjust(10, "*"))  # "*****Hello"
```

## Центрирование строки center
`str.center(width, fillchar=' ')`

### Синтаксис:

string.center(width, fillchar=' ')

### Пример:
```
print(text.center(10, "="))  # "==Hello==="
```

## Примеры во время занятия
```python
text = "Hello"
left_aligned = text.ljust(10)  # Выравнивание по левому краю

print(f"---{left_aligned}---")
print(f"---123456789_123456789_")

right_aligned = text.rjust(10)
print(f"---{right_aligned}---")
print(f"---123456789_123456789_")

center_aligned = text.center(10)
print(f"---{center_aligned}---")
print(f"---123456789_123456789_")
```