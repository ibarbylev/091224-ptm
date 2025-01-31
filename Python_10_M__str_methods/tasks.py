"""
================================== Задача 1 ================================
Приходит текст из 5 строк.
Задача:
 - строка не должна начинаться с пробелов, допустима только табуляция (отступ).
 - сделать так, чтобы все строки начинались с большой буквы;
 - не было подряд несколько пробелов и знаков пунктуации;
Не забывайте, что точка не всегда значит конец предложения! Например, и т.д. и т.п.
"""
text_str = """    \thello,,,, world.    how are you???    
    \t I'm fine, thank   you.     
\tI am fine too!!!     
Do you know what means "и т.д. и т.п."?
   \t   I'm fine. Thank you   for your question!           """


# =============== РЕЗУЛЬТАТ ==================
# 	Hello, world. How are you?
# 	I'm fine, thank you.
# 	I am fine too!
# Do you know what means "и т.д. и т.п."
# 	I'm fine. Thank you for your question!

# решение задачи
UNIQ_MARK = "!№;%:?"
PUNCTUATION_MARKS_AND_SPACE = " ,.:;!?"


""" ================================== Задача 2 ================================ 
Напишите программу, которая запрашивает у пользователя строку и подстроку,
а затем находит все вхождения подстроки в строке и выводит их позиции.
Используйте метод find() для поиска подстроки.
Если подстрока не найдена, выведите соответствующее сообщение на экран.
ПРИМЕЧАНИЕ: поиск должен быть регистронезависимым.

Пример вывода:
Введите строку: Hello, how are you? How's the weather today?
Введите подстроку: How
Подстрока найдена на позициях: 7, 20
"""