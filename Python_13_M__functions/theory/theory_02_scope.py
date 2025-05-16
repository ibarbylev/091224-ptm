count = 0


def outer():
    count = 1
    print("inside the outer function before the inner function", count)

    def inner():
        count = 2
        print("inside the inner function", count)

    inner()
    print("inside the outer function after the inner function", count)


print("before the outer function", count)
outer()
print("after the outer function", count)
