from bs4 import BeautifulSoup
import requests, json, time
from func import *

tick = 0.1
site1 = 'https://lemurrr.ru/catalog/cat/food-nutrition/dry-food'


html = requests.get(site1).text
soup = BeautifulSoup(html, 'lxml')
items = soup.find_all('a', class_='entry__lnk')[0:1]
links = []
data = []
for link in items:
    html = requests.get('https://lemurrr.ru'+link['href']).text

    soup = BeautifulSoup(html, 'lxml')
    reviews = soup.find_all(attrs={"itemprop" : "reviewBody"})[0:3]

    dic = {'title': 'title', 'country': 'country', 'reviews': []}

    for review in reviews:
        dic['reviews'].append(review.text)
        print(review.text)
    data.append(dic)

    time.sleep(tick)

with open("../data/lemur.json", "w") as fp: 
    json.dump(data , fp)