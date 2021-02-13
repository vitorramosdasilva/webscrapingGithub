from urllib.parse import urlsplit
import csv
from csv import reader



# Funcoes ...
def convert_to_bytes(tipo: str, numero:float):

    bytes = 0.0
    if tipo == 'Bytes':
        bytes = float(numero)
    if tipo == 'KB':
        bytes = (float(numero) * float(1024))    
    if tipo == 'MB' or tipo == 'Megabytes':
        bytes = (float(numero) * float(1024) * float(1024))
    if tipo == 'GB' or tipo == 'Gigabytes':
        bytes = (float(numero) * float(1024) * float(1024) * float(1024))
    if tipo == 'TB' or tipo == 'Terabytes':
        bytes = (float(numero) * float(1024) * float(1024) * float(1024) * float(1024))         
 
    return  bytes

def get_extensao(urlSearch:str):
    
    parts = urlsplit(urlSearch)
    paths = parts.path.split('/')
    arquivo = paths[-1]
    tam_arquivo = len(arquivo)
    numberPonto = arquivo.find('.')
    auxN = tam_arquivo - numberPonto
    extensaoUrl = arquivo[-auxN:].replace('.', '')    
    
    return extensaoUrl

def get_first_linguagem(firstlink:str):
    
    firstPage = firstlink
    indexString = firstPage.find('=')
    indexString += 1
    languageFilter = firstPage[indexString:]
        
    return languageFilter


def saveCsv(pageSearch, extensoes_array):
    
    f = csv.writer(open(pageSearch + '.csv', 'w'))
    f.writerow(['Links'])
    for ext in extensoes_array:
        f.writerow([ext])    
    f.close()    
    
    
