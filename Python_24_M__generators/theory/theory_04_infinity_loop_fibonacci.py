def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


N_MAX = 10

fb_gen = fibonacci_generator()
for i in range(N_MAX):
    print(next(fb_gen))
