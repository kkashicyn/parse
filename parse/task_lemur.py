from bs4 import BeautifulSoup
import requests, json, time
from func import *

tick = 0.05
url_base = 'https://lemurrr.ru/catalog/cat/food-nutrition/dry-food'


html = requests.get(url_base).text
soup = BeautifulSoup(html, 'lxml')

last_page = soup.find_all('a', class_='pagenav__button')[-2]
last_page = int(last_page.text)

urls = []
for i in range(1, last_page+1):
    urls.append(url_base+'?page='+str(i))    


#urls = urls[0:1]

links = []
for url in urls:    
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all('a', class_='entry__lnk')
    for link in elements:
        if 'product' in link['href']:
            links.append(link['href'])

    time.sleep(tick)

data = []

links = links[0:10]

for link in links:
    html = requests.get('https://lemurrr.ru'+link).text

    soup = BeautifulSoup(html, 'lxml')
    reviews = soup.find_all(attrs={"itemprop" : "reviewBody"})[0:3]
    title = soup.find('h1').text.strip()

    dic = {'title': title, 'country': '', 'reviews': []}
    for review in reviews:
        dic['reviews'].append(review.text)

    data.append(dic)
    time.sleep(tick)

with open("../data/lemur.json", "w") as fp: 
    json.dump(data , fp)