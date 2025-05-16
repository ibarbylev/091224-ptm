def infinity_counter():
    count = 0
    while True:
        yield count
        count += 1


N_MAX = 10

int_count = infinity_counter()
for i in range(N_MAX):
    print(next(int_count))
