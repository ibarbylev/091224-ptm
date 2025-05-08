"""Новый взгляд на цикл for"""

my_list = [1, 2, 3]

# ------- var 1 ----------
for item in my_list:
    print(item)


# ------- var 2 ----------
lst_iterator = iter(my_list)
while True:
    try:
        print(next(lst_iterator))
    except StopIteration:
        break
