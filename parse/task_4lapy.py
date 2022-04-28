from bs4 import BeautifulSoup
from func import *
import requests, json, time

tick = 0.1

url_base = 'https://4lapy.ru/catalog/koshki/korm-koshki/sukhoy/'

html = requests.get(url_base).text
soup = BeautifulSoup(html, 'lxml')
links = soup.find_all('a', class_='b-common-item__image-link')

last_page = soup.find_all('a', class_='b-pagination__link')[-2]
last_page = int(last_page['title'])

urls = []
for i in range(1, last_page+1):
    urls.append('https://4lapy.ru/catalog/koshki/korm-koshki/sukhoy/?page='+str(i))    

urls =urls[0:1]
links = []
for url in urls:    
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all('a', class_='b-common-item__image-link')
    for link in elements:
        links.append(link['href'])

    time.sleep(tick)

data = []

links = links[0:2]

for link in links:

    html = requests.get("https://4lapy.ru/"+link).text
    soup = BeautifulSoup(html, 'lxml')
    brand = soup.find('a', class_='b-title--h2').text.strip()
    title = soup.find('h1', class_='b-title--h1').text.strip()    
    reviews = soup.find_all('div', class_='b-review__text')[0:3]
    country = soup.find(text='Страна производства').parent.parent.parent.find(class_='b-characteristics-tab__characteristics-value').text.strip()
    # country = soup.find_all('div', class_='b-characteristics-tab__characteristics-value')[7].text.strip()
    dic = {'title': brand + ' ' +  title, 'country': country, 'reviews': []}
    
    for review in reviews:
        dic['reviews'].append(review.text)
    data.append(dic)
    time.sleep(tick)

# save data to json
with open("../data/4lapy.json", "w") as fp: 
    json.dump(data , fp)

