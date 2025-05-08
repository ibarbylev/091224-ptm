from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper's doc_string"""
        print(50 * '*')
        f = func(*args, **kwargs)
        print(50 * '*')
        return f
    return wrapper


# Однако декоратор в Python имеет более удобное обозначение
@decorator
def some_func(comment):
    """Doc_string for some_func"""
    print(f'Something useful...{comment}')
    print(f"The name of our function is ...{some_func.__name__}")
    print(f"The doc_string of our function is ...{some_func.__doc__}")
    return 'RETURN FROM some_func _'


print(some_func('for me'))

# **************************************************
# Something useful...
# **************************************************
