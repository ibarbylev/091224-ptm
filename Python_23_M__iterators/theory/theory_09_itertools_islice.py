import itertools

my_list = [1, 2, 3, 4, 5]
my_iterator = itertools.islice(my_list, 1, 4)
for item in my_iterator:
    print(item)  # Выводит 2, 3, 4


colors = ['red', 'green', 'blue', 'yellow']
sizes = ['S', 'M', 'L']
for x in itertools.zip_longest(colors, sizes, fillvalue='Not exists'):
    print(x)



