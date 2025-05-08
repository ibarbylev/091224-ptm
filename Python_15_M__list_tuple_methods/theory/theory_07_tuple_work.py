"""  tuple work  """

lst: list = [1, 2, 3]

t = tuple(lst)
print(type(t))  # <class 'tuple'>
print(t)   # (1, 2, 3)


""" ======== get item by index ======== """
print(t[0])   # 1


""" ======== change item by index ======== """

try:
    t[0] = "A"
except Exception as e:
    print(f"{e.__class__.__name__}: {e}")
