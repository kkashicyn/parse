from bs4 import BeautifulSoup
from func import *
import requests, time, json

tick = 0.1

url = 'https://www.petshop.ru/catalog/cats/syxkor/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
items = soup.find_all('a', class_='j_product-link')[0:10]

links = []
for item in items:
    links.append(item['href'])
    
links = set(links)    

data = []

for link in links:

    html =requests.get('https://www.petshop.ru'+link).text
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('h1').text.strip()
    review_id = soup.find('div', class_='i-flocktory')['data-fl-item-id']
    dic = {'title': h1, 'country': 'country', 'reviews': []}

    el = requests.get('https://www.petshop.ru/api/v2/site/product/'+review_id+'/reviews/?offset=0&limit=3').json()
    for comment in el['comments']:
        dic['reviews'].append(comment['comment'])
    data.append(dic)
    time.sleep(tick)

# save data to json
with open("../data/petshop.json", "w") as fp: 
    json.dump(data , fp)