""" Функция isinstance() позволяет проверить, является ли объект
экземпляром определенного класса или его потомком.

isinstance() смотрит по всей цепочке наследования вверх —
от класса объекта до самого object, проверяя, есть ли там указанный класс.

Синтаксис:
    isinstance(<исследуемый объект>, <тип, с которым сравнивается исследуемы объект>)

Например:
    isinstance(555, int)
    isinstance(555, (int, float, Decimal))
    isinstance(555, int | float | Decimal)

"""


class Animal:
    pass


class Cat(Animal):
    pass


class Dog(Animal):
    pass

animal = Animal()
cat = Cat()
dog = Dog()


print(isinstance(animal, Animal))   # True
print(isinstance(cat, Animal))      # True
print(isinstance(cat, Cat))         # True
print(isinstance(cat, Dog))         # False
print(isinstance(animal, Dog))      # False
try:
    # 2-й аргумент isinstance() должен быть типа type (или тюплом типов)
    print(isinstance(cat, dog))         # False
except Exception as e:
    print(f'{e.__class__.__name__}: {e} ')


"""mro() - Method Resolution Order (порядок разрешения методов). 
Он используется для определения порядка, в котором 
классы наследуются и методы/атрибуты ищутся в иерархии классов.

__mro__ - атрибут, который работает аналогично методу .mro()
но возвращает тюпл классов, вместо списка классов
"""

print(Animal.mro())
print(animal.__class__.mro())
# [<class '__main__.Animal'>, <class 'object'>]
# [<class '__main__.Animal'>, <class 'object'>]

print(Cat.mro())
print(Dog.__mro__)
# [<class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>]
# (<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)
