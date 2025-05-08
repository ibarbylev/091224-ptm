"""Работа с инкрементными (или in-place) операторами присваивания.

Эти методы используются, если требуется изменяемость (mutable) экземпляров класса.
Если объекты должны быть неизменяемыми (immutable),
то достаточно обычных арифметических методов.
"""


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
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError("Cannot compare amounts with different currencies")
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

    # ============== in-place operators ====================

    def __iadd__(self, other):
        other = self._check_currency(other)
        self.amount += other.amount
        return self

    def __isub__(self, other):
        other = self._check_currency(other)
        self.amount -= other.amount
        return self

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.amount *= other
            return self
        return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            self.amount /= other
            return self
        return NotImplemented

    # ==================================

    def __str__(self):
        return f"{self.amount} {self.currency}"


# Примеры использования
money1 = Money(50, "USD")
one = Money(1, "USD")


money1 += one
print(money1)
money1 -= one
print(money1)
money1 *= 5
print(money1)
money1 /= 5
print(money1)
