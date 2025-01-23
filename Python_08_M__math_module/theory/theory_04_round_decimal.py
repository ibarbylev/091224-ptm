from decimal import Decimal, ROUND_HALF_UP

number = Decimal('3.14159')

# Определяем точность до 2 знаков после запятой
rounded_number = number.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP)

print(f"Original number: {number}")
print(f"Rounded number using quantize: {rounded_number}")

# Original number: 3.14159
# Rounded number using quantize: 3.14

# ===========================================================

# Округляем до 2 знаков после запятой с помощью функции round
rounded_number = round(number, 2)

print(f"Original number: {number}")
print(f"Rounded number using round: {rounded_number}")

# Original number: 3.14159
# Rounded number using quantize: 3.14
