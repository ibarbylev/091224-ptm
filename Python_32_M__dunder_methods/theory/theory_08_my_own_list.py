class CustomList:
    def __init__(self, *args):
        self.items = list(args)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# ====== делаем ТОЛЬКО СВОЮ конкатенацию списков ======
    def __add__(self, other):
        return CustomList(*list(set(self.items) | set(other.items)))


# Примеры использования
clist = CustomList(1, 2, 3, 4, 5)
clist2 = CustomList(1, 2, 3, 4, 5, 6)

print(clist)  # Вывод: [1, 2, 3, 4, 5]

# Получение элемента
print(clist[2])  # Вывод: 3

# Установка элемента
clist[2] = 10
print(clist)  # Вывод: [1, 2, 10, 4, 5]

# Удаление элемента
del clist[2]
print(clist)  # Вывод: [1, 2, 4, 5]

# Длина списка
print(len(clist))  # Вывод: 4

# Конкатенация списков
print(clist + clist2)
