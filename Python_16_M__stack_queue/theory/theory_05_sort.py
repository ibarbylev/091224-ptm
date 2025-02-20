# print(help(list.sort))

def key_sort(x):
    return x[0]


my_list = [(2, 'cv'), (1, 'd'), (2, 'cc')]
my_list.sort(key=key_sort)
print(my_list)  # [(1, 'd'), (2, 'cv'), (2, 'cc')]


lst = ['aac', 'aab', 'aaa']
lst.sort()
print(lst)  # ['aaa', 'aab', 'aac']
