"""
================================== Задача 1 ================================
Приходит текст из 5 строк.
Задача:
 - строка не должна начинаться с пробелов, допустима только табуляция (отступ).
 - сделать так, чтобы все предложения начинались с большой буквы;
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

lines = text_str.split('\n')
new_text = ''
i = 0
while i < len(lines):
    line = lines[i]
    line = line.replace("и т.д. и т.п.", UNIQ_MARK)
    # - строка не должна начинаться с пробелов, допустима только табуляция (отступ).
    line_lst = line.split("\t")
    print(line_lst)     # ['   ', "   I'm fine. Thank you   for your question!           "]
    j = 0
    new_line = ''
    while j < len(line_lst):

        j += 1

    # - сделать так, чтобы все предложения начинались с большой буквы;
    # - не было подряд несколько пробелов и знаков пунктуации;
    # - Не забывайте, что точка не всегда значит конец предложения! Например, и т.д. и т.п.

    line = line.replace(UNIQ_MARK, "и т.д. и т.п.")
    new_text += line + '\n'
    i += 1

print(new_text)
