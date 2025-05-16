import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f"Execution time {func.__name__} {execution_time:.2f} s")
    return wrapper


@timer
def loop(num):
    lst = []
    for n in range(num):
        lst.append(n)
    return lst


@timer
def list_comp(num):
    return [n for n in range(num)]


if __name__ == "__main__":
    number = 10000000
    loop(number)
    list_comp(number)
