class Car:
    quantity = 0

    def __init__(self, brand):
        self.brand = brand
        Car.quantity += 1


wv = Car('WV')
print(wv.quantity)  # 1
toyota = Car('Toyota')
print(toyota.quantity)  # 2
print(wv.quantity)      # 2

# Попробуем изменить атрибут класса из экземпляра класса
toyota.quantity = 10
print(toyota.quantity)  # 10

# Попробуем значения атрибутов экземпляров класса
print(wv.__dict__)       # {'brand': 'WV'}
print(toyota.__dict__)   # {'brand': 'Toyota', 'quantity': 10}

# Вывод: мы НЕ изменили атрибут класса quantity
# Мы просто добавили новый атрибут к экземпляру класса toyota
# Который теперь закрывает (экранирует) доступ к атрибуту класса quantity
# из экземпляра класса.
# Но мы можем обойти экранирование, обратившись к классу с помощью метода .__class__
print(toyota.__class__.quantity)  # 2
