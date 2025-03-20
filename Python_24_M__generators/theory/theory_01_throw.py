def my_generator():
    try:
        yield 1
        yield 2
    except ValueError as e:
        # Здесь может быть код, который запустится после получения исключения
        print(f"{e.__class__.__name__}: {e}")


gen = my_generator()
print(next(gen))  # Выводит 1
if next(gen) < 3:
    try:
        gen.throw(ValueError("Specially thrown exception"))
    except StopIteration as e:
        # с методом .throw генератор завершается нестандартно!
        print(f"{e.__class__.__name__}: {e}")




