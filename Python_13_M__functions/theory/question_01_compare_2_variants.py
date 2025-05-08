# ============== variant 1 ====================
def smth_1():
    i = 100
    print(i)


i = 1
for _ in range(10):
    if i % 2 == 0:
        print(i)
    else:
        smth_1()
    i += 1


print(" ============== variant 2 ==================== ")


def smth_2():
    global i
    i = 100
    print(i)


i = 1
for _ in range(10):
    if i % 2 == 0:
        print(i)
    else:
        smth_2()
    i += 1