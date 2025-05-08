from decimal import Decimal, getcontext, localcontext, Context, ROUND_HALF_UP

# Создание пользовательского контекста вычислений
# ВНИМАНИЕ! Точность 5 относится КО ВСЕМ значимым цифрам,
# а не к цифрам после запятой!
custom_context = Context(prec=5, rounding=ROUND_HALF_UP)

# Пример числа для округления
number = Decimal('3.1415926')

# Округление числа с использованием пользовательского контекста
rounded_number = custom_context.create_decimal(number)

print(f"Original number: {number}")
print(f"Rounded number using custom context: {rounded_number}")
# Original number: 3.1415926
# Rounded number using custom context: 3.1416


# Использование пользовательского контекста для выполнения арифметических операций
with localcontext(custom_context):
    # Округление числа до 4 знаков после запятой с использованием quantize
    rounded_number = number.quantize(Decimal('1.0000'), rounding=ROUND_HALF_UP)
    result = Decimal('1') / Decimal('3')
    print(result)  # 0.33333


# Вне контекста вычисление идёт с точностью по умолчанию, то есть 28 знаков
result2 = Decimal('1') / Decimal('3')
print(result2)  # 0.3333333333333333333333333333
