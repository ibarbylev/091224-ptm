from typing import Generator, Iterable, Iterator, Callable
from types import FunctionType


x = [1, 2, 3]

print(isinstance(x, Generator))
print(isinstance(x, Iterable))
print(isinstance(x, Iterator))
print(isinstance(x, Callable))
