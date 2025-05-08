class CustomDict:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)


cdict = CustomDict()
cdict['name'] = 'Alice'
cdict['age'] = 30
print(cdict)  # Вывод: {'name': 'Alice', 'age': 30}

# Получение элемента
print(cdict['name'])  # Вывод: Alice

# Установка элемента
cdict['age'] = 31
print(cdict)  # Вывод: {'name': 'Alice', 'age': 31}

# Удаление элемента
del cdict['name']
print(cdict)  # Вывод: {'age': 31}

# Длина словаря
print(len(cdict))  # Вывод: 1
