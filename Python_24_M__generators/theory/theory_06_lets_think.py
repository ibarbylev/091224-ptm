def test():
    s = 0
    while True:
        x = yield s
        s += x


t = test()
print(next(t))
print(t.send(111))
print(t.send(123))
