"""Тернарный оператор -
позволяет сократить условное выражение до одной строки.

выражение1 if условие else выражение2

"""

value = input('Введите "True" или "False": ')
if value == "True":
    value_bool = True
else:
    value_bool = None


value_bool = True if value == "True" else False

print("value = ", value)
print("value_bool = ", value_bool)
