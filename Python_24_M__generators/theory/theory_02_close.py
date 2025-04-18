def my_generator():
    try:
        yield 1
        yield 2
    except GeneratorExit as e:
        # Код для очистки ресурсов
        print(f"{e.__class__.__name__}: {e}")


gen = my_generator()
print(next(gen))  # Выводит 1
if next(gen) < 3:
    gen.close()
print('End of script execution')



