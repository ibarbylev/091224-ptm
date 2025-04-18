""" What will this code do? """


def message(times):
    if times > 0:
        print('Это рекурсивная функция')
        message(times - 1)
        print(times)


message(5)





