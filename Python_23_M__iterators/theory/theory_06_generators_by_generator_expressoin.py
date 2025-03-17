"""Зачем нужна предварительная инициализация генератора перед использованием?"""


# декларация генератора
def gen():
    yield 1
    yield 2
    yield 3


# и декларация, и инициализация генератора одновременно
g = (x for x in range(1, 4))

try:
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())

except StopIteration as e:
    print(e)  # Exit from generator
else:
    print("Прерывание по StopIteration не произошло!")
