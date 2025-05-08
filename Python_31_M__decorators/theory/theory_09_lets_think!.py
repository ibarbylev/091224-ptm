"""Давайте подумаем: "Что происходит в этом коде"? """


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def print_some_text():
    return 'some_text'


print(print_some_text())
