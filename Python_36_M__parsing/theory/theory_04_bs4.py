"""https://beautiful-soup-4.readthedocs.io/en/latest/"""


import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/REST"

response = requests.get(URL)
if response.status_code == 200:

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # Извлечение заголовков
    titles = soup.find_all("h2")
    for title in titles:
        print(title)
    print('============================================')

    # Извлечение текста заголовков
    for title in titles:
        print('title.text:', title.text)
    print('============================================')

    # Извлечение текста параграфа
    paragraph = soup.find("p")
    print('paragraph:', paragraph)
    print('paragraph.text:', paragraph.text)
    print('============================================')

    # Извлечение ссылки
    tag_a = soup.find("a")
    print('tag_a:', tag_a)
    print('tag_a.text:', tag_a.text)
    print('tag_a.attrs:', tag_a.attrs)
    print('tag_a["href"] =', tag_a["href"])
    print('tag_a.get("href") =', tag_a.get("href"))
    print('tag_a.get("class") =', tag_a.get("class"))


