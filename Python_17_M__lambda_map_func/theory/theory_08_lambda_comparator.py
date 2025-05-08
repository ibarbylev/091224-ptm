lst = [('aa', 3), ('av', 2), ('ab', 1), ('aa', 1)]
print(lst)


lst.sort(key=lambda x: x[0][1])
print(lst)


def f(x):
    return x[0][1]


lst.sort(key=f)
print(lst)
