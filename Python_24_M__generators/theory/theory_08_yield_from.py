def numbers_gen():
    yield 1
    yield 2
    yield 3
    print('---------')


def letters_gen():
    yield 'a'
    yield 'b'
    yield 'c'
    print('---------')


gen = letters_gen()


def combined_gen():
    yield from numbers_gen()
    yield from gen
    yield from [10, 20, 30]


# Использование combined_gen для итерации по всем значениям
for value in combined_gen():
    print(value)


print(""" ============= Если бы не было выражения yield from ============= """)


def combined_gen_2():
    for value in numbers_gen():
        yield value
    for value in gen:
        yield value
    for value in [10, 20, 30]:
        yield value


for value in combined_gen_2():
    print(value)
