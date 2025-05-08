"""1. Оператор break

Оператор break используется для немедленного выхода из цикла.
Когда выполнение доходит до этого оператора, цикл прекращается,
и управление передается к следующей строке кода после цикла.
"""

for i in range(5):
    if i == 3:
        break  # Прерывает цикл, когда i равно 3
    print(i)

# 0
# 1
# 2

"""2. Оператор continue

Оператор continue используется для пропуска оставшейся части текущей итерации цикла 
и перехода к следующей итерации. 
Цикл не завершится, но текущая итерация будет пропущена, если условие continue выполнено.
"""

for i in range(3):
    if i == 1:
        continue  # Пропускает итерацию, когда i равно 3
    print(i)

# 0
# 2

""" 3. Оператор else в цикле for

Оператор else в цикле выполняется, если цикл завершился естественно, 
то есть без использования оператора break.
Если цикл был прерван с помощью break, блок else не выполнится.
"""
# ======== var 1 =========
for i in range(5):
    if i == 3:
        print("Found 3, breaking the loop.")
        break
else:
    print("This won't be printed, when the loop was broken.")

# Found 3, breaking the loop.


# ======== var 2 =========
for i in range(3):
    if i == 3:
        print("Found 3, breaking the loop.")
        break
else:
    print("This won't be printed, when the loop was broken.")

# This won't be printed, when the loop was broken
