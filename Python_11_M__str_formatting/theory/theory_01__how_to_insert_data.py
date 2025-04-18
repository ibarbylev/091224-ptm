""" ============================ .format() ===================================== """

# аргументы по умолчанию
print("Hello {}, your balance is {}.".format("Adam", 230.2346))

# позиционные аргументы
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))

# аргументы ключевые слова
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))

# смешанные аргументы
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))

""" ============================ f-string ===================================== """

name, blc = "Adam", 230.2346
print(f"Hello {name}, your balance is {blc}.")


""" ============================ c-string =====================================
%d - для целых целых чисел
%f - для вещественных чисел 
%s - для строк
"""

name, age, height = "Ivan", 30, 1.82
print(f"Hello %s! You're %d years old and your height is %f." % (name, age, height))
print(f"Hello %s! You're %d years old and your height is %.2f meters." % (name, age, height))
