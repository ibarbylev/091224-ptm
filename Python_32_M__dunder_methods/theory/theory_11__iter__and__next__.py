from typing import Iterable, Iterator, List


class CustomIterator:
    def __init__(self, data: List):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


class CustomIterable:
    def __init__(self, data: List):
        self.data = data

    def __iter__(self):
        return CustomIterator(self.data)

    def __str__(self):
        return f'{list(self.data)}'


# Создаём объект-итератор
cust_it = CustomIterable([1, 2, 3])
print(isinstance(cust_it, Iterable))
print(isinstance(cust_it, Iterator))
print('cust_it = ', cust_it)

cust_iterator = iter(cust_it)
print(isinstance(cust_iterator, Iterable))
print(isinstance(cust_iterator, Iterator))
print('cust_iterator = ', cust_iterator)


print(next(cust_iterator))  # Вывод: 1
print(next(cust_iterator))  # Вывод: 2
print(next(cust_iterator))  # Вывод: 3
try:
    print(next(cust_iterator))  # Здесь произойдет StopIteration
except StopIteration:
    print("Iteration is complete")  # Вывод: Iteration is complete
