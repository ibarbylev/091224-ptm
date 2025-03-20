from typing import Generator, Iterable, Iterator, Callable

g = (x for x in range(1, 4))

def gen():
    yield 1
    yield 2
    yield 3

g2 = gen()

def gen2():
    for i in range(1, 4):
        yield i

g22 = gen2()

def gen3():
    yield from range(1, 4)

g3 = gen3()

print(isinstance(g2, Generator))
print(isinstance(g2, Iterable))
print(isinstance(g2, Iterator))
print(isinstance(g2, Callable))
