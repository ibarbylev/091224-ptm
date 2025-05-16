import requests

# Ссылка для скачивания изображения (можно также открыть для просмотра в браузере):

IMG_URL = 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Guido_van_Rossum_OSCON_2006.jpg/250px-Guido_van_Rossum_OSCON_2006.jpg'

response = requests.get(IMG_URL)

filename = 'Guido_van_Rossum_OSCON_2006.jpg'
with open(filename, 'wb') as f:
    f.write(response.content)

"""
В результате файл с ликом Великого Гвидо ван Россума сохраняется с текущем каталоге
"""
