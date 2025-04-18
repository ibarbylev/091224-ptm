"""Tower of Hanoi

https://upload.wikimedia.org/wikipedia/commons/6/60/Tower_of_Hanoi_4.gif?20050322192703

Идея рекурсивной функции для решения задачи Ханойских башен основывается на разбиении задачи на более простые подзадачи.
В частности, перемещение n дисков с одного стержня на другой можно свести к последовательности шагов,
каждый из которых решает меньшую задачу.

Вот основные шаги и принципы, лежащие в основе рекурсивного алгоритма:

    Базовый случай: Если у нас только один диск, переместить его напрямую с исходного стержня на целевой.
    Рекурсивный случай: Если дисков больше одного:
        Переместить n-1 дисков с исходного стержня на вспомогательный, используя целевой стержень как вспомогательный.
        Переместить оставшийся (самый большой) диск с исходного стержня на целевой.
        Переместить n-1 дисков с вспомогательного стержня на целевой, используя исходный стержень как вспомогательный.

(ВНИМЕНИЕ! Для запуска скрипта необходимо использовать терминал ОС, а не IDE!)
"""

import os
import time


def clear_screen():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Unix/Linux/MacOS/BSD/etc
    else:
        os.system('clear')


def get_color(disk):
    colors = [
        "\033[31m",  # Красный
        "\033[32m",  # Зеленый
        "\033[33m",  # Желтый
        "\033[34m",  # Синий
        "\033[35m",  # Фиолетовый
        "\033[36m",  # Голубой
    ]
    return colors[(disk - 1) % len(colors)]


def draw_towers(towers, total_height):
    clear_screen()
    for i in range(total_height - 1, -1, -1):
        for tower in towers:
            if i < len(tower):
                disk = tower[i]
                color = get_color(disk)
                print(color + str(disk).center(10) + "\033[0m", end=' ')
            else:
                print('|'.center(10), end=' ')
        print()
    print('-' * 30)


def hanoi(n, source, target, auxiliary, towers, total_height):
    if n > 0:
        hanoi(n - 1, source, auxiliary, target, towers, total_height)

        disk = towers[source].pop()
        towers[target].append(disk)
        draw_towers(towers, total_height)
        time.sleep(1)
        input('For the next move - press "Enter"!')

        hanoi(n - 1, auxiliary, target, source, towers, total_height)


# Начальные условия
num_disks = 6  # Можно изменить количество дисков
towers = [list(range(num_disks, 0, -1)), [], []]
total_height = num_disks + 1  # Высота должна включать стержень
draw_towers(towers, total_height)
time.sleep(1)
hanoi(num_disks, 0, 2, 1, towers, total_height)
