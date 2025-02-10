count = 0


def outer():
    print("inside the outer function before the inner function", count)
    count = 10  # Переменная в охватывающей Enclosing (но не глобальной) области видимости
    print("inside the outer function before the inner function", count)

    def inner():
        nonlocal count  # Указываем, что x берется из внешней функции
        count = 20  # Меняем значение x в outer

    inner()
    print(count)  # 20


print(count)
outer()
print(count)
