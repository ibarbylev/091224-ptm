def my_generator():
    received_value = 0
    received_value = yield 1
    print(received_value)
    received_value = 1 if received_value is None else received_value
    yield received_value + 1


print(' ===== without send method ===== ')
gen = my_generator()
print(next(gen))      # Выводит 1
print(next(gen))      # Выводит 1


print(' ===== with send method ===== ')
# gen = my_generator()
# # print(next(gen))      # Выводит 1
# print(gen.send(10))
# print(gen.send(10))   # Выводит 11





