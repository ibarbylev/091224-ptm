print(" =================== function sorted() and reversed() ========================== ")
my_list = [3, 1, 2]
print(my_list)
sorted_list = sorted(my_list)
reversed_list = list(reversed(my_list))

print(sorted_list)  # Выводит [1, 2, 3]
print(reversed_list)  # Выводит [2, 1, 3]
print(my_list == sorted_list)
print(my_list == reversed_list)
print()

print(" =================== .sort() and .revers() ========================== ")
print(my_list.sort())
print(my_list)

print(my_list.reverse())
print(my_list)
