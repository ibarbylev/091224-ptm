from typing import Callable


def decorator(func):
    def wrapper():
        print(50 * '*')
        func()
        print(50 * '*')
    return wrapper


# Однако декоратор в Python имеет более удобное обозначение
@decorator
def some_func():
    print(f'Something useful...')


some_func()

# **************************************************
# Something useful...
# **************************************************
