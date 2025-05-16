num = 10

lst_1 = []
for n in range(num):
    lst_1.append(n)
print(lst_1)


lst_2 = [n for n in range(num)]
print(lst_1)

""" =========== if condition =========== """
nums = list(range(10))
print(nums)

even_nums = [n for n in nums if n % 2 == 0]
print(even_nums)


""" =========== if else condition =========== """
even_and_double_odd_nums = [n if n % 2 == 0 else n * 2 for n in nums]
print(even_and_double_odd_nums)

