"""Допустим, нам необходима гарантия, что x и y строго положительные числа
Вариант 1:
 - условие в __init__()
 - геттеры и сеттеры
"""
from pprint import pprint


class A:
    def __init__(self, x, y):
        if x < 0:
            raise ValueError("Attribute <x> must be positive")
        if y < 0:
            raise ValueError("Attribute <y> must be positive")

        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value <= 0:
            raise ValueError("Attribute <x> must be positive")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value <= 0:
            raise ValueError("Attribute <y> must be positive")
        self._y = value


# Пример использования
a = A(10, 5)
a.x = 3     # OK
# a.y = -2  # ValueError: y должно быть больше нуля

"""Минусы - дублирование кода

Избежать этого можно с помощью Дескриптора Positive:
"""


class Positive:
    def __set_name__(self, owner, name):
        print(f"__set_name__ called with owner={owner.__name__}, name={name}")
        self.name = '_' + name  # будем хранить значение под другим именем

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"Attribute <{self.name[1:]}> must be positive")
        setattr(instance, self.name, value)

"""
Здесь имя атрибута автоматически определяется с помощью метода __set_name__,
специально применяемого с версии Python 3.6 для дескрипторов.

 - self.name = "_" + name - чтоб избежать бесконечной рекурсии, имя атрибута "x" меняется на "_x"
   Иначе вызов b.x вызовет дескриптор, который вызовет b.x и так до бесконечности
   А вызов b._x просто вызовет атрибут "_x", у которого нет дескриптора 
   
 - owner - Класс, в котором объявлен дескриптор (в нашем случае - B)
 
 - instance - Экземпляр класса, в котором объявлен дескриптор (в нашем случае b)
 
 - методы getattr() и setattr() используются для получения / установки значения атрибута,
   как альтернатива прямого обращения с помощью dot-notation,
   чтобы избежать бесконечной рекурсии

"""


class B:
    x = Positive()
    y = Positive()

    def __init__(self, x, y):
        self.x = x
        self.y = y


pprint(B.__dict__)
# 'x': <__main__.Positive object at 0x7f1e304b1e80>,
# 'y': <__main__.Positive object at 0x7f1e304b1cd0>})
""" Таким образом, x и y - экземпляры класса Positive, 
встроенные в класс B для управления соответствующими его атрибутами
"""


b = B(5, 7)

print(b.x)  # 1

# Контроль изменения значения атрибута на недопустимое (< 0)
try:
    b.x = -5
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")

# Контроль создания объекта с недопустимыми значениями
try:
    b2 = B(-5, 7)
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")
