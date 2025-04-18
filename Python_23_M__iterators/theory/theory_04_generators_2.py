"""Зачем нужна предварительная инициализация генератора перед использованием?"""


# декларация генератора
def gen():
    yield 1
    yield 2
    yield 3


# initiate generator (инициализация генератора)
g = gen()

try:
    print(gen().__next__())
    print(gen().__next__())
    print(gen().__next__())
    print(gen().__next__())
    print(gen().__next__())

except StopIteration as e:
    print(e)
else:
    print("Прерывание по StopIteration не произошло!")

"""Вопрос также решается с помощью цикла for"""

for g in gen():
    print(g)
