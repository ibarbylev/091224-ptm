class Cat:
    def __init__(self, name=''):
        if name:
            self.name = name
        else:
            self.name = "Anonymous"

    def eat(self):
        print(f'A cat named {self.name} is eating.')


cat_1 = Cat('Ryzhik')
cat_1.eat()
cat_2 = Cat()
cat_2.eat()
