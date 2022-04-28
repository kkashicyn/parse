from bs4 import BeautifulSoup
from func import *
import requests, time, json

tick = 0.1

url_base = 'https://www.petshop.ru/catalog/cats/syxkor/'
html = requests.get(url_base).text
soup = BeautifulSoup(html, 'lxml')
links = soup.find_all('a', class_='j_product-link')[0:10]

#page-navigation
paging_block = soup.find('div', class_='page-navigation')
last_page = paging_block.findChildren("a" , recursive=False)[-2]
last_page = int(last_page.text)

urls = []
for i in range(1, last_page+1):
    urls.append('https://www.petshop.ru/catalog/cats/syxkor/?page='+str(i))   

links = []
for url in urls:    
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all('a', class_='inner')
    for link in elements:
        links.append(link['href'])

    time.sleep(tick)

data = []

for link in links:

    html =requests.get('https://www.petshop.ru'+link).text
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('h1').text.strip()
    review_id = soup.find('div', class_='i-flocktory')['data-fl-item-id']
    dic = {'title': h1, 'country': '', 'reviews': []}

    el = requests.get('https://www.petshop.ru/api/v2/site/product/'+review_id+'/reviews/?offset=0&limit=3').json()
    for comment in el['comments']:
        dic['reviews'].append(comment['comment'])
    data.append(dic)
    time.sleep(tick)

# save data to json
with open("../data/petshop.json", "w") as fp: 
    json.dump(data , fp)