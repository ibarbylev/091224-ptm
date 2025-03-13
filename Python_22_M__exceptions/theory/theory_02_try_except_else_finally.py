try:
    y = 10 / int(input("Введите число: "))
except ValueError:
    print("Ошибка! Вероятно вы ввели не число.")
except ZeroDivisionError:
    print("Ошибка деления на ноль")
except Exception as e:
    print(e)
else:
    print(f"Результат: {y}\n"
          f"(Содержимое блока else печатается, ТОЛЬКО если нет ошибки в блоке try.\n"
          f"И НЕ печатается, если ошибка есть)")
finally:
    print("Содержимое блока finally печатается в любом случае")

