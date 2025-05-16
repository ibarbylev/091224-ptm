"""Задание"""


def concat_str(*args: str) -> str:
    result = ''
    for arg in reversed(args):
        result += arg
    return result


print(concat_str('a', 'b', 'c'))
# 'cba'

print(concat_str('ff', 'bb'))
# 'bbff'

