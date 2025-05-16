"""Объясните, что происходит в этом фрагменте кода и какой будет вывод:"""


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("The animal makes a sound")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def make_sound(self):
        super().make_sound()
        print("The dog barks")


my_dog = Dog("Buddy")
my_dog.make_sound()
