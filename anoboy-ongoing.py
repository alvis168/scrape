from bs4 import *
import requests
import json

page = requests.get("https://anoboy.stream/category/anime/ongoing/")
soup = BeautifulSoup(page.content, 'html.parser')

quote = soup.find_all('div', class_='amv')
for q in quote:
    x = soup.find('div', class_='column-content')
    title = q.find ('h3').text
    link = x.find('a').get('href')
    imagelink = q.find ('amp-img').get('src')

    print(title)
    print(link)
    print(imagelink)
