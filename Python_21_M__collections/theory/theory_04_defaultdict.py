from collections import defaultdict

my_dict = defaultdict(int)
my_dict["apple"] = 5
print(my_dict["apple"])  # Выводит 5

print(my_dict["banana"])
# Выводит 0, так как ключа "banana" нет, но defaultdict автоматически создал его со значением 0


my_dict = defaultdict(list)
my_dict["apple"] = [5]
print(my_dict["apple"])  # Выводит [5]

print(my_dict["banana"])
# Выводит [], так как ключа "banana" нет, но defaultdict автоматически создал его со значением 0
