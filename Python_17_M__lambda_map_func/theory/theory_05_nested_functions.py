def outer_function():
    def inner_function():
        print("Inner function")
    inner_function()


outer_function()  # Выводит "Inner function"
