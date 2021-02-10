import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


# def ready_txt():
#     filepath = 'repositories.txt'
#     with open(filepath) as fp:
#         line = fp.readline()
#         cnt = 1
#         while line:
#             print("Line {}: {}".format(cnt, line.strip()))
#             line = fp.readline()
#             cnt += 1
#     return line


# linhas = ready_txt()

# def page_index:
# Collect and parse first page
page = requests.get('https://github.com/vitorramosdasilva/dashboard-genghiscode')
soup = BeautifulSoup(page.text, 'html.parser')
data_links = []

# Create .txt
f = csv.writer(open('results.txt', 'w'))
f.writerow(['Links'])

for li_tag in soup.find_all('ul', {'class': 'list-style-none'}):
    for span_tag in li_tag.find_all('li', {'class': 'd-inline'}):
        link_items = span_tag.find_all('a')
        for links in link_items:
            link = links.get('href')
            linguagem = span_tag.find_all('span')[0].get_text()
            percentagem = span_tag.find_all('span')[1].get_text()
            # print(linguagem, percentagem, link)
            data_links.append('https://github.com' + link + '\n')


# print(data_links)
# f.writerow(data_links)



# for webpage in data_links:
url = 'https://github.com/vitorramosdasilva/dashboard-genghiscode/search?l=Python'
idxLanguage = url.find('=')
idxLanguage += 1
languageFilter = url[idxLanguage:]
page = requests.get('https://github.com/vitorramosdasilva/dashboard-genghiscode/search?l=Python')
soup = BeautifulSoup(page.text, 'html.parser')
contagem = []
linguagem = []
df = pd.DataFrame()
qtd_total = 0
percentual = []


for ul_tag in soup.find_all('ul', {'class': 'filter-list small'}):
    for li_tag in ul_tag.find_all('li'):
        for a_tag in li_tag.find_all('a', {'class': 'filter-item'}):
            for span_tag in a_tag.find_all('span', {'class': 'count'}):
                quantidade = a_tag.text.split('\n')[1]
                contagem.append(int(quantidade.replace(',', '')))
                linguagem.append(a_tag.text.split('\n')[2])
                qtd_total += int(quantidade.replace(',', ''))



                # pegar valor da longuagem filter...

df['linguagem'] = linguagem
df['contagem'] = contagem


for index, row in df.iterrows():
    percentual.append(str(round(float(row['contagem']) / float(qtd_total) * 100, 2)) + '%')
    print(qtd_total, row['contagem'])


df['percentual'] = percentual
print(df)

# if linguagem_search == languageFilter :
#     for div_tag in soup.find_all('div', {'class': 'd-flex flex-column flex-md-row flex-justify-between border-bottom pb-3 position-relative'}):
#         for h3_tag in div_tag.find_all('h3'):
#             contagem = h3_tag.text.replace(' code results in ', '')
#             # print(linguagem, float(contagem.replace(',', '.')))
#             # print(qtd_total)

# 0. LER A DOCUMENTAÇÃO ...
# 1. CRIAR GIT HUB
# 2. Pegar o valor da linguaguem Selecionada
# 3. iTEGAR COM OS LINKS DA PAGINA ...
# 4. PEGAR A QUANTIDADE DE LINHAS DAS PAGINAS DA LINGUAGUEM ...
# 5 CUSPIR NO TXT


# Extensão   |     Linhas    |    Bytes
# js         |  17599 (96 %) | 31894 (79 %)
# md         |    202 ( 1 %) |     5 ( 0 %)
# html       |    130 ( 0 %) |  5703 (14 %)
# json       |     95 ( 0 %) |   465 ( 1 %)
# sh         |     75 ( 0 %) |   101 ( 0 %)
# <outros>   |     74 ( 0 %) |  1322 ( 3 %)
# sample     |     34 ( 0 %) |   787 ( 1 %)
# enc        |      0 ( 0 %) |     3 ( 0 %)
