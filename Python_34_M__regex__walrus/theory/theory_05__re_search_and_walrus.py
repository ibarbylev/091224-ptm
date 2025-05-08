import re

text = "Python is an amazing programming language."
pattern = "amazing"

match = re.search(pattern, text)
if match:
    print("Совпадение найдено:", match.group())
else:
    print("Совпадение не найдено")

# if match := re.search(pattern, text):
#     print("Совпадение найдено:", match.group())
# else:
#     print("Совпадение не найдено")
