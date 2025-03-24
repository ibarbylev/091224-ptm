"""Добавьте в генератор square_generator() обработку исключений ValueError и GeneratorExit.
И корректно обработайте эти исключения в основном коде.

Исключение ValueError передаётся в генератор с помощью метода throw().
При получении этого исключения, генератор должен вывести на печать фразу:
    "Исключение успешно обработано!"
И затем продолжить свою обычную работу.

Исключение GeneratorExit вызывается методом close().
"""


def square_generator():
    pass


gen = square_generator()

# Инициализация генератора
next(gen)

print(gen.send(3))  # 9
print(gen.send(4))  # 16

# Вброс исключения ValueError в генератор
try:
    print("gen.throw", gen.throw(ValueError("Throw an exception into the generator")))  # 1
except StopIteration as e:
    print(f"{e.__class__.__name__}: {e}")

print(next(gen))    # 1
print(gen.send(3))  # Output: 9
print(gen.send(4))  # Output: 16
print(gen.send(5))  # Output: 25

# Закрытие генератора
gen.close()

