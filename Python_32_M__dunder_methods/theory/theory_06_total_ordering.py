"""Метод @functools.total_ordering позволят автоматически
создавать методы сравнения (__lt__, __le__, __gt__, __ge__)
на основе метода равенства (__eq__) и
ещё одного метода больше или меньше (__gt__ или __lt__).

"""

from functools import total_ordering


@total_ordering
class Person:
    def __init__(self, name, iq):
        self.name = name
        self.iq = iq

    def __str__(self):
        return f'Person({self.name}, {self.iq})'

    def __eq__(self, other):
        return self.iq == other.iq

    def __lt__(self, other):
        return self.iq < other.iq


john = Person('John', 120)
mike = Person('Mike', 125)

print(john == mike)
print(john != mike)
print(john >= mike)
print(john > mike)
print(john <= mike)
print(john < mike)

