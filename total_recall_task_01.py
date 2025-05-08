"""Сколько уникальных слов находится на этой странице:
https://en.wikipedia.org/wiki/REST
При решении необходимо использовать регулярные выражения.
"""

import re
import requests

URL = "https://en.wikipedia.org/wiki/REST"

response = ...
uniq_words = 0


print(f"There are {len(uniq_words)} unique words on the {URL} website.")
#  There are 1750 unique words on the https://en.wikipedia.org/wiki/REST website.
