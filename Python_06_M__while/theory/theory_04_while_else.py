"""Конструкция else после цикла while позволяет
выполнить блок кода, когда
    - условие цикла (после while) становится ложным.

Если цикл завершился c прерыванием с помощью break,
то код в блоке else НЕ будет выполнен.
"""

count = 2
while count < 2:
    print(count)
    count += 1
else:
    print("Цикл завершен")


# 2 =====================
# count = 2
# while count < 2:
#     print(count)
#     count += 1
# else:
#     print("Цикл завершен")

# 3 =====================
# count = 0
# while count < 2:
#     print(count)
#     count += 1
#     if count == 2:
#         break
# else:
#     print("Цикл завершен")


