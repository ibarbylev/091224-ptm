# ДИНАМИЧЕСКОЕ ФОРМАТИРОВАНИЕ
# динамический шаблон формата строки
string = "{:{fill}{align}{width}}"

# передача кодов формата в качестве аргументов
print(string.format('cat', fill='*', align='^', width=5))

# динамический шаблон формата float
num = "{:{align}{width}.{precision}f}"

# передача кодов формата в качестве аргументов
print(num.format(123.236, align='<', width=8, precision=2))

# ============================ f-string =====================================
text, n_fl = 'cat', 123.236
print(f"{text:10}|")
print(f"{text:>10}| >")
print(f"{text:^10}| ^")
print(f"{text:<10}| <")
print(f"{text:=>10}| >")
print(f"{text:*^10}| ^")
print(f"{text:-<10}| <")
print()
print(f"{n_fl:9.2f}| f")
print(f"{n_fl:>9.2f}| >f")
print(f"{n_fl:^9.2f}| ^f")
print(f"{n_fl:<9.2f}| <f")
print(f"{n_fl:0>9.2f}| >f")
print(f"{n_fl:=^9.2f}| ^f")
print(f"{n_fl:-<9.2f}| <f")

"""
*cat*
123.24  
cat       |
       cat| >
   cat    | ^
cat       | <
=======cat| >
***cat****| ^
cat-------| <

   123.24| f
   123.24| >f
 123.24  | ^f
123.24   | <f
000123.24| >f
=123.24==| ^f
123.24---| <f
"""


