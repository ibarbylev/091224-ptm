# Метод `replace()` - метод замены подстроки в строке.

`str.replace(old, new[, count])`

### Описание:
Метод .replace() возвращает новую строку, в которой old заменён на new.
Если указан count, заменит только первые N вхождений.

### Синтаксис:

`string.replace(old, new, count=-1)`

    old – подстрока, которую нужно заменить.
    new – строка, на которую будет произведена замена.
    count (необязательно) – максимальное число замен (по умолчанию заменяет все).

### Пример 1 – замена всех вхождений:
```
text = "apple banana apple"
print(text.replace("apple", "orange"))  
# "orange banana orange"
```
### Пример 2 – замена только 1 раза:
```
print(text.replace("apple", "orange", 1))  
# "orange banana apple"
```
### Пример 3 – если old не найден:
```
print(text.replace("grape", "pear"))  
# "apple banana apple" (без изменений)
```