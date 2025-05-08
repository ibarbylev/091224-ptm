"""__str__ человекочитаемое описание объекта (для пользователей).
   __repr__ - для программиста (чтобы однозначно воссоздать объект по описанию)
   Желательно оформлять __repr__ таким образом,
   чтобы eval(repr(cat)) возвращал бы экземпляр класса

   Если нет __str__, то в print() отображается __repr__.
   Если есть оба - _str__

  https://www.digitalocean.com/community/tutorials/python-str-repr-functions
"""


class Cat:
    def __init__(self, name=""):
        if name:
            self.name = name
        else:
            self.name = "Anonymous"

    def __str__(self):
        return f'The cat named {self.name}'

    def __repr__(self):
        return f'Cat(name={self.name!r})'

    def eat(self):
        print(f'A cat named {self.name} is eating.  ест.')


cat = Cat('Ryzhik')
print('__str__():', cat)
print('__repr__():', repr(cat))

# __str__(): The cat named Ryzhik
# __repr__(): Cat(name='Ryzhik')

new_instance = eval(repr(cat))
print('new_instance:', new_instance)
print('type(new_instance):', type(new_instance))
print(isinstance(eval(repr(cat)), Cat))

# new_instance: The cat named Ryzhik
# type(new_instance): <class '__main__.Cat'>
# True
