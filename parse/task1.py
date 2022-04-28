from bs4 import BeautifulSoup
import requests, time, json

site = 'https://feedsmart.ru/suhoy-korm-dlya-koshek'
html = requests.get(site).text
soup = BeautifulSoup(html, 'lxml')

data = []
divs = soup.find_all('div', class_='korm-element')    

for div in divs:

    title = div.find('div', class_='title').text.strip()    
    rank = div.find('div', class_='ratings').find('div', class_='overall').find('div', class_='num').text.strip()
    data.append({'title': title, 'rank': rank})
# save data to json

with open("../data/marks.json", "w") as fp: 
    json.dump(data , fp)




    
