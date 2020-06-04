from bs4 import *
import requests
import json

page = requests.get("https://anoboy.stream/category/anime/ongoing/")
soup = BeautifulSoup(page.content, 'html.parser')

quote = soup.find_all('div', class_='column-content')
for q in quote:
    #x = soup.find_all('div', class_='column-content')
    #title = q.find ('title').text
    #link = q.find('a').get('href')
    imagelink = q.find ('amp-img').get('src')

    #print(title)
    #print(link)
    print(imagelink)
