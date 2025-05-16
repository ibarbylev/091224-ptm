"""Packing
Знак *, по сути, "упаковывает" все переданные в функцию аргументы в один tuple.
Отсюда и название:  Packing
"""


def concat_str(*args):
    print(args)
    print(type(args))   # <class 'tuple'>

    for arg in args:
        print(arg)


concat_str(1, 2, 3, 4, 5, 6, 7)
