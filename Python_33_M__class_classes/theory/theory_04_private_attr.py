class MyClass:
    def __init__(self, temperature):
        if 10 < temperature < 30:
            self.__temperature = temperature
        else:
            raise ValueError(f'Incorrect temperature value {temperature}!')

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if 10 < value < 30:
            self.__temperature = value
        else:
            raise ValueError(f'Incorrect temperature value {value}!')


m = MyClass(25)
try:
    # Вызов приватного атрибута через экземпляр класса невозможен
    print(m.__temperature)
except AttributeError as e:
    print('AttributeError:', e)


print(m.temperature)  # 25
m.temperature = 29
print(m.temperature)

try:
    m.temperature = 30
except ValueError as e:
    print(e)  # Incorrect temperature value 30!


# Тем не менее, есть способ обойти этот запрет напрямую изменить private метод:
m._MyClass__temperature = 35
print(m._MyClass__temperature)
