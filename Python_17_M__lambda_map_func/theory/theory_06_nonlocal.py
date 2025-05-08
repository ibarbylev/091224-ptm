def outer_function():
    x = 1

    def inner_function():
        nonlocal x
        x = 2
    inner_function()
    print(x)  # Выводит 2


outer_function()

try:
    print(x)
except Exception as e:
    print(e)

