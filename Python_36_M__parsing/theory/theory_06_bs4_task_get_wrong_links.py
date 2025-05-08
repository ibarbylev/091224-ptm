"""А теперь найдите ссылки, которые находятся внутри
блока div и класса "wrong-links"
"""

from bs4 import BeautifulSoup


def get_html(filename: str) -> str:
    pass


html_content = get_html('example_navbar_links.html')
soup = BeautifulSoup(html_content, 'html.parser')

wrong_div = ...



pass



# <a href="https://wrong-site-1.com">Wrong link 1</a>
# <a href="https://wrong-site-2.com">Wrong link 2</a>
# <a href="https://wrong-site-3.com">Wrong link 3</a>
# <a href="https://wrong-site-4.com">Wrong link 4</a>
# <a href="https://wrong-site-5.com">Wrong link 5</a>
