"""Написать программу, которая скачивает страницу с сайта на выбор
с актуальным курсом валют, выделяет курс доллара к евро и выводит его.
Можно пользоваться регулярными выражениями и Beautiful Soup вместе.

Уточнение: используйте html-код файла <example_table.html>
"""

from bs4 import BeautifulSoup


def get_html(filename: str) -> str:
    with open(filename, encoding='utf-8') as f:
        return f.read()


html_content = get_html('example_table.html')
soup = BeautifulSoup(html_content, 'html.parser')

table = soup.table
rows = table.find_all('tr')
for row in rows:
    items = row.find_all('td')
    if items:
        _, code, _, currency, value = items
        print(code.text.strip(), currency.text.strip(), value.text.strip())
        if code.text == 'USD':
            usd = float(value.text.replace(',', '.'))
        if code.text == 'EUR':
            eur = float(value.text.replace(',', '.'))

print(f'Курс USD / EUR = {usd / eur}')
# AUD Австралийский доллар 58,0043
# AZN Азербайджанский манат 51,7600
# AMD Армянских драмов 22,6655
# BYN Белорусский рубль 28,1601
# BGN Болгарский лев 49,1738

# Курс USD / EUR = 0.9244371976920589
