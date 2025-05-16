def my_generator():
    value = yield
    if value > 0:
        yield value * 2
    else:
        yield value * 3


gen = my_generator()
print(next(gen))
print(gen.send(5))    # Выводит 10
# print(gen.send(-2))   # Выводит -6
