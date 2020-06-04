
import requests
import json
from bs4 import *

    page=requests.get("https://anoboy.stream/")
    soup=BeautifulSoup(page.content,'html.parser')
    lis=soup.find('div',class_='amvj')
    for q in lis:
        imagelink=q.find('amp-img').get('src')
        #animelink=baseurl+li.find('a').get('href')
        title=q.find('h3').text
        print(title)
        #print(animelink)
        print(imagelink)
