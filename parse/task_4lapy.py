from bs4 import BeautifulSoup
from func import *
import requests, json, time

tick = 0.1

url = 'https://4lapy.ru/catalog/koshki/korm-koshki/sukhoy/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
links = soup.find_all('a', class_='b-common-item__image-link')[1:10]

data = []

for link in links:

    html = requests.get("https://4lapy.ru/"+link['href']).text
    soup = BeautifulSoup(html, 'lxml')
    brand = soup.find('a', class_='b-title--h2').text.strip()
    title = soup.find('h1', class_='b-title--h1').text.strip()    
    reviews = soup.find_all('div', class_='b-review__text')[0:3]
    country = soup.find_all('div', class_='b-characteristics-tab__characteristics-value')[7].text.strip()
    dic = {'title': brand + title, 'country': country, 'reviews': []}
    
    for review in reviews:
        dic['reviews'].append(review.text)
    data.append(dic)
    time.sleep(tick)

# save data to json
with open("../data/4lapy.json", "w") as fp: 
    json.dump(data , fp)

