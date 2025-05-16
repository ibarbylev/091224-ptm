from typing import Callable


def some_func():
    print('Something useful...')


def decorator(func):
    def wrapper():
        print(50 * '*')
        func()
        print(50 * '*')
    return wrapper


# Теперь функция decorator действительно - декоратор!
print(isinstance(decorator(some_func), Callable))  # True

# Поэтому для её вызова нужно добавить скобки:
decorator(some_func)()

# **************************************************
# Something useful...
# **************************************************
