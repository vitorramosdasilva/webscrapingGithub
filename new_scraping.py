import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = 'https://github.com/vitorramosdasilva/dashboard-genghiscode'
page = requests.get(url)
    
soup = BeautifulSoup(page.text, 'html.parser')
links_array = []
linguagem_array = []
extensoes_array = []


# Obtem os primeiro link de procura das linguagens
# Se não exisitir link
for li_tag in soup.find_all('ul', {'class': 'list-style-none'}):
    for span_tag in li_tag.find_all('li', {'class': 'd-inline'}):
        link_items = span_tag.find_all('a')
        for links in link_items:
            link = links.get('href')            
            links_array.append('https://github.com' + link)


#print(links_array)
#print(links_array[0])


#Obtenho todas as extensões do projeto ..
page = requests.get(links_array[0])
soup = BeautifulSoup(page.text, 'html.parser')
for ul_tag in soup.find_all('ul', {'class': 'filter-list small'}):
    for li_tag in ul_tag.find_all('li'):
        for a_tag in li_tag.find_all('a', {'class': 'filter-item'}):
            for span_tag in a_tag.find_all('span', {'class': 'count'}):
                linguagem_array.append(a_tag.text.split('\n')[2].replace('              ',''))
                # print(linguagem_array[0])
                # qtd_total += int(quantidade.replace(',', ''))
                # print(contagem[0])                
                # print(qtd_total)


# Encontrando a primeira linguagem pesquisada e inserindo na lista de Extensões ...
firstPage = links_array[0]
indexString = firstPage.find('=')
indexString += 1
languageFilter = firstPage[indexString:]

linguagem_array.append(languageFilter)
total_paginas = 1
 
# print(languageFilter)            
# print(linguagem_array)
# print(len(linguagem_array))
# d-flex d-md-inline-block pagination

# page = requests.get(urlSearch)
# soup = BeautifulSoup(page.text, 'html.parser')
# for em_tag in soup.find_all('em', {'class': 'current'}):    
#     total_paginas = em_tag['data-total-pages']
   

# Todas a paginas para search .....
for pageSearch in linguagem_array:
    
    for em_tag in soup.find_all('em', {'class': 'current'}):    
    total_paginas = int(em_tag['data-total-pages'])
    
    urlSearch = url + '/search?l=' + pageSearch
    if total_paginas or total_paginas > 0:
        urlSearch = url + '/search?l=' + pageSearch + '&p=' + total_paginas++
    
    page = requests.get(urlSearch)
    soup = BeautifulSoup(page.text, 'html.parser')
    for div_tag in soup.find_all('div', {'class': 'width-full'}):           
        for div1_tag in div_tag.find_all('div', {'class': 'f4 text-normal'}):
            a_tag = div1_tag.find_all('a')            
            for links in a_tag:   
                link = links.get('href')
                extensoes_array.append('https://github.com' + link) 

        
# print(extensoes_array) 
# print(len(extensoes_array)) 
    

        
   
        
       
           
