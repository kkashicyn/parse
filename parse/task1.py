from bs4 import BeautifulSoup
import requests, time

site = 'https://feedsmart.ru/suhoy-korm-dlya-koshek'
html = requests.get(site).text
soup = BeautifulSoup(html, 'lxml')

# find last page of catalog
# last_page = soup.find('li', class_='pager-last').find('a')
# last_page = last_page['href'].split('?')[0]
# last_page = int(last_page.split('/')[-1])

# create list with data from parsing

# for i in range(1,last_page):    
list_with_data = []
divs = soup.find_all('div', class_='korm-element')    

for div in divs:

    title = div.find('div', class_='title').text.strip()    
    rank = div.find('div', class_='ratings').find('div', class_='overall').find('div', class_='num').text.strip()
    list_with_data.append({'title': title, 'rank': rank})
#print count of items in list_with_data
print(len(list_with_data))


# create html document
html_doc_begin = "<html><body><table>"
html_inner = ""
for item in list_with_data:
    html_inner += "<tr><td>"+item['title']+"</td><td>"+item['rank']+"</td></tr>"

html_doc_end = "</table></body></html>"

html = html_doc_begin + html_inner + html_doc_end

# save html document    
with open('table1.html', 'w') as f:
    f.write(html)


    
