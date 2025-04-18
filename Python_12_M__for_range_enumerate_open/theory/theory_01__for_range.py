"""Цикл for используется для перебора каждого элемента
в итерируемом объекте (списке, строке, диапазоне и т. д.).
."""

# 1. Итерация по списку
for item in ['apple', 'banana', 'orange']:
    print(item)

# apple
# banana
# orange


# 2. Итерация по символам строки
for symbol in 'word':
    print(symbol, end=', ')  # w, o, r, d,

# 3. Итерация по диапазону чисел
for i in range(5):
    print(i, end=', ')  # 0, 1, 2, 3, 4,


for i in range(2, 5):
    print(i, end=', ')  # 2, 3, 4,


for i in range(0, 10, 2):
    print(i, end=', ')  # 0, 2, 4, 6, 8,


for i in range(10, 0, -2):
    print(i, end=', ')  # 10, 8, 6, 4, 2,

