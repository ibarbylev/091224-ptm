from pprint import pprint
from collections import Counter, OrderedDict

text = """
В качестве текста использовать текст этой задачи. 

Необходимо посчитать сколько раз встретилось каждое слово и вывести в топ слов, 
упорядоченный сначала по убыванию встречаемости, 
а при равенстве частот в соответствии с упорядочиванием в лексикографическом порядке. 

Слова должны быть переведены в нижний регистр и из них должны быть удалены все небуквенные символы.

Решить задачу с помощью использования изученных классов.
"""

words: list[str] = text.lower().split()

# Clear words from punctuation marks
for i, word in enumerate(words):
    words[i] = ''.join([s for s in word if s.isalpha()])


words_dict = dict(Counter(words))
print(type(words_dict))

# words_dict_sort = dict(sorted(words_dict.items(), key=lambda x: x[1]))
words_dict_sort = OrderedDict(sorted(words_dict.items(), key=lambda x: (-x[1], x[0])))

pprint(words_dict_sort)
