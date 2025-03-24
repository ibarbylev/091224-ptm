from bisect import bisect_left, bisect_right

data1 = [1, 3, 5, 7, 9]
data2 = [1, 3, 6, 7, 9]

index = bisect_left(data1, 6)  # Результат: 3
print(index)
index = bisect_right(data1, 6)  # Результат: 3
print(index)

index = bisect_left(data2, 6)  # Результат: 2
print(index)
index = bisect_right(data2, 6)  # Результат: 3
print(index)



