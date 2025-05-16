from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper's doc_string"""
        print(50 * '*')
        f = func(*args, **kwargs)
        print(50 * '*')
        return f
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper's doc_string"""
        print(50 * '=')
        f = func(*args, **kwargs)
        print(50 * '=')
        return f
    return wrapper


@decorator1
@decorator2
def some_func():
    print('printing some_func _')


some_func()
