from decimal import Decimal, getcontext

getcontext().prec = 10  # Установка точности на 10 знаков после запятой
number1 = Decimal('1') / Decimal('7')
print(number1)  # 0.1428571429
#                   1234567890
