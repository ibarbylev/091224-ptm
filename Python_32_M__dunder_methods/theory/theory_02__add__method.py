class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        raise ValueError("Cannot add amounts with different currencies")
        # return NotImplemented

    def __str__(self):
        return f"{self.amount} {self.currency}"


m1 = Money(100, "eur")
m2 = Money(230, "eur")
m3 = m1 + m2
print(m3.__dict__)  # {'amount': 330, 'currency': 'eur'}

m1 = Money(100, "eur")
m2 = Money(230, "eur")
m4 = Money(230, "usd")
try:
    m5 = m1 + m4
    print(m5)
except Exception as e:
    print(f'{e.__class__.__name__}("{e}")')
    # ValueError("Cannot add amounts with different currencies")


# 330 eur
# {'amount': 330, 'currency': 'eur'}

# ValueError("Cannot add amounts with different currencies")
