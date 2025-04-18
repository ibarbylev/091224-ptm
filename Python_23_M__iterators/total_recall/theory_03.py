"""Что бы вы изменили в это коде?"""

try:
    x = 10 / 0
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")
except ArithmeticError as e:
    print(f"{e.__class__.__name__}: {e}")
except ZeroDivisionError as e:
    print(f"{e.__class__.__name__}: {e}")

