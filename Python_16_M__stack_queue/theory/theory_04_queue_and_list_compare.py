from collections import deque
from theory_02_list_comprehension_and_list_compare import timer


@timer
def var_list(num):
    lst = []
    for i in range(num):
        lst.append(i)
        # print(lst)
    for i in range(num):
        lst.pop(0)
        # print(lst)


@timer
def var_deque(num):
    queue = deque()
    for i in range(num):
        queue.append(i)
        # print(queue)
    for i in range(num):
        queue.popleft()
        # print(queue)


n = 50000
var_list(n)
var_deque(n)
