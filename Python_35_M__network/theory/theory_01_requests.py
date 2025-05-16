from pprint import pprint

import requests

URL = "https://it4each.com"
response = requests.get(URL)
print(response.status_code)  # Выводит код состояния ответа
print(50 * '=')

print(response.text[:500])  # Выводит данные, полученные от сервера (первый 500 символов)
print(50 * '=')

pprint(dict(response.headers))  # Выводит словарь заголовков
