class Cat:
    def __init__(self, name, tail: int):
        self.name = name
        self.tail = tail

    def __bool__(self):
        return self.tail != 0

    def __len__(self):
        return self.tail

    def __hash__(self):
        return hash(self.__str__())

    def __str__(self):
        return f'A cat called {self.name} with a tail length of {self.tail} sm.'


cat = Cat('Marusja', 25)
print(cat)
print('len(cat) =', len(cat))
print('hash(cat) =', hash(cat))
print('bool(cat) =', bool(cat))
print()

cat2 = Cat('Murzik', 0)
print(cat2)
print('len(cat2) =', len(cat2))
print('hash(cat2) =', hash(cat2))
print('bool(cat2) =', bool(cat2))
