from decimal import Decimal, getcontext


print(""" =========== числа, с точностью, указанной в аргументе =========== """)
number1 = Decimal('0.1')
number2 = Decimal('0.2')
result = number1 + number2
print(result)  # 0.3

print(""" =========== числа, со стандартной точностью decimal =========== """)

number1 = Decimal(0.1)
number2 = Decimal(0.2)
result = number1 + number2
print(result)  # 0.3000000000000000166533453694
#                  123456789_123456789_123456789_
print(getcontext().prec)  # 28 знаков

print(""" =========== То же самое с помощью Decimal.from_float(x: float) =========== """)
number1 = Decimal.from_float(0.1)
number2 = Decimal.from_float(0.2)
result = number1 + number2
print(result)  # 0.3000000000000000166533453694
#                  123456789_123456789_123456789_
