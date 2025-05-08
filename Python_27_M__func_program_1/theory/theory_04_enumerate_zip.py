from typing import Iterator


fruits = ['apple', 'banana', 'orange']

""" ====================== enumerate ======================= """
enum_obj = enumerate(fruits)
print(enum_obj)  # <enumerate object at 0x7f21a3ed7f10>
print(*enum_obj)
print(isinstance(enum_obj, Iterator))  # True

""" ====================== zip ======================= """
zip_obj = zip(range(3), fruits)
print(zip_obj)  # <zip object at 0x7f7c9675bf80>
print(*zip_obj)
print(isinstance(zip_obj, Iterator))  # True
