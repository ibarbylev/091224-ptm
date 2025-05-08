class Cat:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'Кот {self.name} ест.')


cat = Cat('Ryzhik')
cat.eat()
