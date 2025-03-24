"""К самой первой  задаче (# 1) добавьте новое условие:
Если число отрицательное, то оно возводится в третью степень
"""


def square_generator():
    pass


gen = square_generator()
# Инициализация генератора
next(gen)

print(gen.send(3))   # 9
print(gen.send(-4))  # -64
print(next(gen))     # 1
print(next(gen))     # 1
print(gen.send(-5))  # 125
