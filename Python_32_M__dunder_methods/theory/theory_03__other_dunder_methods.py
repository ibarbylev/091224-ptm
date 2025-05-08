class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def _check_currency(self, other):
        if not isinstance(other, Money):
            raise TypeError("Operand must be of type Money")
        if self.currency != other.currency:
            raise ValueError("Cannot operate on amounts with different currencies")
        return other

    def __add__(self, other):
        other = self._check_currency(other)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        other = self._check_currency(other)
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Money(self.amount * factor, self.currency)
        return NotImplemented

    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)):
            return Money(self.amount / divisor, self.currency)
        return NotImplemented

    def _compare_currency(self, other):
        if not isinstance(other, Money):
            raise TypeError("Operand must be of type Money")
        if self.currency != other.currency:
            raise ValueError("Cannot operate on amounts with different currencies")
        return other

    def __eq__(self, other):
        other = self._compare_currency(other)
        return self.amount == other.amount

    def __lt__(self, other):
        other = self._compare_currency(other)
        return self.amount < other.amount

    def __le__(self, other):
        other = self._compare_currency(other)
        return self.amount <= other.amount

    def __gt__(self, other):
        other = self._compare_currency(other)
        return self.amount > other.amount

    def __ge__(self, other):
        other = self._compare_currency(other)
        return self.amount >= other.amount

    def __str__(self):
        return f"{self.amount} {self.currency}"


# Примеры использования
money1 = Money(50, "USD")
money2 = Money(20, "USD")
money3 = Money(100, "EUR")

print(money1 + money2)  # Вывод: 70 USD
print(money1 - money2)  # Вывод: 30 USD
print(money1 * 2)       # Вывод: 100 USD
print(money1 / 2)       # Вывод: 25 USD

print(money1 == money2)  # Вывод: False
print(money1 > money2)   # Вывод: True

try:
    print(money1 == money3)  # Вывод: ValueError: Cannot compare amounts with different currencies
except Exception as e:
    print(e)

try:
    print(money1 < money3)   # Вывод: ValueError: Cannot compare amounts with different currencies
except Exception as e:
    print(e)

try:
    money1 += 1             # Вывод: 'int' object has no attribute 'currency'
except Exception as e:
    print(e)