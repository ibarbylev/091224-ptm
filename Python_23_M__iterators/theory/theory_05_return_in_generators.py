"""Зачем нужна предварительная инициализация генератора перед использованием?"""


# декларация генератора
def gen():
    yield 1
    yield 2
    yield 3
    return "Exit from generator"


# initiate generator (инициализация генератора)
g = gen()

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
