from pprint import pprint

import requests

URL = "https://it4each.com"
response = requests.get(URL)
print(response.cookies)  # Выводит cookie, полученные от сервера
pprint(dict(response.cookies))  # Выводит cookie, полученные от сервера

cookies = {"session_id": "bv3jyqjnejtf444vpz4muqv6tplh1dpx"}
response = requests.get(URL, cookies=cookies)


