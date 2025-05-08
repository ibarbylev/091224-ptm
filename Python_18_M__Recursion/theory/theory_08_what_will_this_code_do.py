""" What will this code do? """


def message(times):
    if times > 0:
        print('Это рекурсивная функция')
        print(times)
        message(times - 1)


message(5)





