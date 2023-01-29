import requests
from bs4 import BeautifulSoup
from collections import Counter

url = 'https://greenatom.ru/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/108.0.0.0 YaBrowser/23.1.1.1135 Yowser/2.5 Safari/537.36'}

request = requests.get(url, headers=header)
print(f'Результат выполнения Get запроса: {request.ok}')

if request.ok:
    page = request.text
    soup = BeautifulSoup(page, 'html.parser')
    counter = Counter([tag.name for tag in soup.find_all(True)])
    print(f'Колличество Html-тегов в коде: {sum(counter.values())}')

    tags_with_attributes = 0
    for key, val in counter.items():
        for i in range(val):
            if soup.find_all(key)[i].attrs:
                tags_with_attributes += 1
    print(f'Колличество Html-тегов с атрибутами: {tags_with_attributes}')