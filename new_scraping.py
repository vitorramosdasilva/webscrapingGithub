import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from funcoes import *


myTxt = open("repositories.txt", "r")
qt_linha = 0
qt_bk = 0
ext_array = []
linha_array = []
kabaite_array = []    

for url in myTxt:
    ext_url = 'https://github.com/' + str(url.replace('\n',''))
    page = requests.get(ext_url)
    if page.status_code != 200:
        page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    my_link = '' 
    linguagem_array = [] # Todas As Linguagens do Repositorio para utilizar na pagina de Search
    extensoes_array = [] # Todas url da pagina Serach
    total_paginas = [] # Todas de Paginas para Cada Pagina de Search Linguagem ..


    
    # Se não exisitir a Barra de Progresso da Linguagem saio do Loop .. 
    span = soup.find_all('span', {'class': 'Progress-item'}) 
    if not span:
       print('Ops um caso sem lista de Linguagens, vamos para o próximo...') 
       continue
    
    # Obtem os primeiro link de procura das linguagens
    for li_tag in soup.find_all('ul', {'class': 'list-style-none'}):
        for span_tag in li_tag.find_all('li', {'class': 'd-inline'}):
            link_items = span_tag.find_all('a')
            for links in link_items:
                link = links.get('href')
                my_link = 'https://github.com' + link
                break
    # print(links_array)
    # print(links_array[0])


    # Obtenho todas as extensões do projeto ..
    page = requests.get(my_link)
    soup = BeautifulSoup(page.text, 'html.parser')
    for ul_tag in soup.find_all('ul', {'class': 'filter-list small'}):
        for li_tag in ul_tag.find_all('li'):
            for a_tag in li_tag.find_all('a', {'class': 'filter-item'}):
                for span_tag in a_tag.find_all('span', {'class': 'count'}):
                    linguagem_array.append(a_tag.text.split('\n')[2].replace('              ', ''))
                    # print(linguagem_array[0])                   
                    # print(contagem[0])
             


    # Encontrando a primeira linguagem pesquisada e inserindo na lista de Linguagens ...

    languageFilter = get_first_linguagem(my_link)
    linguagem_array.append(languageFilter.title())
    # print(languageFilter)
    # print(linguagem_array)
    # print(len(linguagem_array))


    # Obtenho a quantidade total de paginas de cada linguagem..
    for pageSearch in linguagem_array:
        urlSearch = ext_url + '/search?l=' + pageSearch + '&p=1'
        page = requests.get(urlSearch, timeout=(3.05, 27))
        if page.status_code != 200:
            page = requests.get(urlSearch, timeout=(3.05, 27))

        soup = BeautifulSoup(page.text, 'html.parser')

        for em_tag in soup.find_all('em', {'class': 'current'}):
            total_paginas.append(em_tag['data-total-pages'] + '|' + pageSearch)
            

    # Obtenho total de paginas (sem a quantidade de paginas, isso é com apenas uma pagina) de cada linguagem..
    for pageSearch in linguagem_array:
        urlSearch = ext_url + '/search?l=' + pageSearch + '&p=1'
        page = requests.get(urlSearch, timeout=(3.05, 27))
        if page.status_code != 200:
            page = requests.get(urlSearch, timeout=(3.05, 27))

        soup = BeautifulSoup(page.text, 'html.parser')
        if not soup.find_all("em", {"class": "current"}):
            total_paginas.append('0' + '|' + pageSearch)
    # print(total_paginas)


    # Insiro as Listas de Linguagens e Total de Páginas Atualizadas nas Listas
    list_ling = []
    list_tot_pag = []
    for i in total_paginas:
        list_tot_pag.append(int(i.split('|')[0]))
        list_ling.append(i.split('|')[1])
    # print(list_ling)
    # print(list_tot_pag)


    # Todas a paginas para search .....
    for index, pageSearch in enumerate(list_ling):
        
        tot_pag = list_tot_pag[index]
        if tot_pag == 0:
            tot_pag = 1

        i = 1
        while i <= tot_pag:
            urlSearch = ext_url + '/search?l=' + pageSearch + '&p=' + str(i)
            # print(urlSearch)
            page = requests.get(urlSearch, timeout=(3.05, 27))
            time.sleep(1.5)
            # Se perder alguma url aumenta pra 3 no sleep...
            if page.status_code != 200:
                page = requests.get(urlSearch, timeout=(3.05, 27))

            soup = BeautifulSoup(page.text, 'html.parser')
            for div_tag in soup.find_all('div', {'class': 'width-full'}):
                for div1_tag in div_tag.find_all('div', {'class': 'f4 text-normal'}):
                    a_tag = div1_tag.find_all('a')[0]
                    link = a_tag.get('href')
                    extensoes_array.append('https://github.com' + link)
                    # print(link)             

            i += 1


    cont = 0
    # extensoes_array = []  
    # extensoes_array.append('https://github.com/frontpressorg/frontpress/blob/99f91d8718b8e2573108f57f8508f8186fef5d9f/ci/travis_deploy.sh')
    for urlSearch in extensoes_array:
        # print(urlSearch)
        page = requests.get(urlSearch, timeout=(3.05, 27))
        # time.sleep(1)
        if page.status_code != 200:
            page = requests.get(urlSearch, timeout=(3.05, 27))

        soup = BeautifulSoup(page.text, 'html.parser')
        count = 0
        for div_tag in soup.find('div', {'class': 'text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0'}):
                                            
            conteudo = str(div_tag).split()
            # print(conteudo)
            count += 1
            # print('count' + str(count))            
            if count == 1 or count == 5:                 
                try:                       
                    linha = int(conteudo[0])
                    linha_array.append(linha) 
                    # Chamo o metodo para obter a Extensao e Insiro na Lista
                    ext_array.append(get_extensao(urlSearch))
                    qt_linha += linha
                except:    
                    print('linha (index) não existe nessa rodada : ' + urlSearch)
                    # print('linha' + linha)
            if count == 3 or count == 7:
                try:
                    numero = float(conteudo[0]) 
                    tipo =  conteudo[1]
                    # print('tipo: ' + str(tipo))
                    # print('numero: ' + str(numero))
                    my_byte = convert_to_bytes(tipo,numero)
                    kabaite_array.append(my_byte)
                    qt_bk += my_byte              
                    # print('kb' + kabaites)
                except:
                    print('bytes (index) não existe nessa rodada : ' + urlSearch)                        
                    print('tipo de bytes (index) não existe nessa rodada : ' + urlSearch)
if ext_array:
    df = pd.DataFrame()
    df['Extensão'] = ext_array
    df['Linhas'] = linha_array
    df['Bytes'] = kabaite_array  
    print('quantidade de arquvos capturados: ' + str(len(linha_array)))
    
     
    df_sum = df.groupby(['Extensão']).sum()   
    df_sum['% '+'Linhas'] = round((df_sum['Linhas'] / qt_linha)*100,2)
    df_sum['% '+'Bytes'] = round((df_sum['Bytes'] / qt_bk)*100,2)
   
       
    # Gera novo .txt e Escreve os dados ...
    file = open("Output.txt", "w")
    file.close()
    df_sum.reset_index().to_csv('Output.txt', index=False)
   
else:
    
    print('Não há casos com listas de linguagens nessas urls para gerar Output.txt ...')  
   

print(df_sum)
print('Fim do Processo ....')
