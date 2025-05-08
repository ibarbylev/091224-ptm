from typing import Callable


def decorator(func):
    def wrapper():
        """Wrapper's doc_string"""
        print(50 * '*')
        func()
        print(50 * '*')
    return wrapper


# Однако декоратор в Python имеет более удобное обозначение
@decorator
def some_func():
    """Doc_string for some_func"""
    print(f'Something useful...')
    print(f"The name of our function is ...{some_func.__name__}")
    print(f"The doc_string of our function is ...{some_func.__doc__}")


some_func()

# **************************************************
# Something useful...
# **************************************************
