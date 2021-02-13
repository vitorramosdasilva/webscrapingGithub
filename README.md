# webscrapingGithub
webscraping dos repositórios do Github a partir das informações em um arquivo .txt e exportada as informações em outro .txt

Passo a Passo para Execução:
1.  Clone o projeto
2. Na pasta raiz do projeto há um arquivo repositories.txt e nele há o nome do projeto do GitHub exemplo:

  frontpressorg/frontpress
  SambitAcharya/Mini-Projects
  
Nas informaçoes acima demonstra o <nomedousuario/nomedoprojeto>.
Inserindo informações nesse arquivo .txt a ferramenta de webScraping coletara os dados de repositório.

3. Para Executar o projeto insira no terminal: python3 new_scraping.py 
4. Ao final da execução ele salva no arquivo OutPut.txt os dados:

 Extensão       Linhas      Bytes  % Linhas    % Bytes
                                              
LICENSE             19    1064.96      7.57     424.29
css                285    4469.24    113.55    1780.57
csv                 32     817.00     12.75     325.50
htaccess             2      63.00      0.80      25.10
html               175    6260.76     69.72    2494.33
js                 296    7255.36    117.93    2890.58
json               131    2835.28     52.19    1129.59
lock                68    2160.64     27.09     860.81
md                 344   15124.48    137.05    6025.69
minjs                4   95744.00      1.59   38145.02
php               1999   55701.08    796.41   22191.67
py                1943   63023.12    774.10   25108.81
scrutinizeryml       7     147.00      2.79      58.57
travisyml           18     267.00      7.17     106.37
txt              15645  466776.80   6233.07  185966.85


5. Ao final da execução ele gera a quantidade total de arquivos capturados no terminal
6. Ao final da execução ele gera a informação de (processo terminado) no terminal
