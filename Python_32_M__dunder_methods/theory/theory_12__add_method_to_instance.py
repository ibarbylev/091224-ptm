from pprint import pprint
import types  # пакет для работы с внутренними типами


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car = Car('WV', 'Passat')
# car.info = lambda: print(f"{car.brand} {car.model}")
car.__setattr__('info', lambda: print(f"{car.brand} {car.model}"))

car.info()
# WV Passat

# формально это добавляет метод, но только статический
# и только в конкретный экземпляр класса
pprint([attr for attr in car.__dir__() if not attr.startswith('__')])

# Экземпляр с другим именем даст ошибочный резульатат:
t = Car('Toyota', 'Camry')
t.__setattr__('info', lambda: print(f"{car.brand} {car.model}"))
t.info()  # WV Passat


# Добавление self тоже ничего не даст:
# (интерпретатор просто "не поймёт", что такое self)
try:
    t.__setattr__('info', lambda self: print(f"{self.brand} {self.model}"))
    t.info()  # WV Passat
except Exception as e:
    print(f'{e.__class__.__name__}: {e}')
    # NameError: name 'self' is not defined

# С помощью types.MethodType() можно добавить метод к классу без конструктора


def info(self):
    print(f"{self.brand} {self.model}")


t.__setattr__('info', types.MethodType(info, t))
t.info()  # Toyota Camry

# Можно также добавить новый метод сразу к классу:
setattr(Car, 'info', info)

bmw = Car('BMW', 'X6')
bmw.info() # Toyota Camry



