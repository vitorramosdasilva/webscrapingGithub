# WebscrapingGithub
webscraping dos repositórios do Github a partir das informações em um arquivo .txt e exportada as informações em outro .txt

Passo a Passo para Execução:
1.  Clone o projeto
2. Na pasta raiz do projeto há um arquivo repositories.txt e nele há o nome do projeto do GitHub exemplo:

  frontpressorg/frontpress
  SambitAcharya/Mini-Projects
  
Nas informaçoes acima demonstra o <nomedousuario/nomedoprojeto>.
Inserindo informações nesse arquivo .txt a ferramenta de webScraping coletara os dados de repositório.

3. Para Executar o projeto insira no terminal: python3 new_scraping.py 
4. Ao final da execução ele salva no arquivo Output.txt na raiz do projeto os dados, exemplo:


|Extensão       |  Linhas    |  Bytes      | % Linhas  | % Bytes|
| ------------- | ---------- | ----------- | --------- | -------|
|LICENSE        |  19        | 1064.96     | 0.05      | 0.07   |
|configjs       |  38        | 873.00      | 0.10      | 0.06   |
|confjs         |  76        | 2570.24     | 0.20      | 0.17   |
|constantjs     |  16        | 538.00      | 0.04      | 0.04   |
|controllerjs   |  412       | 14099.40    | 1.06      | 0.94   |
|css            |  285       | 4469.24     | 0.73      | 0.30   |
|csv            |  32        | 817.00      | 0.08      | 0.05   |
|directivejs    |  320       | 8531.00     | 0.82      | 0.57   |
|editorconfig   |  13        | 190.00      | 0.03      | 0.01   |
|filterjs       |  12        | 243.00      | 0.03      | 0.02   |
|gitignore      |  12        | 242.00      | 0.03      | 0.02   |
|htaccess       |  2         | 63.00       | 0.01      | 0.00   |
|html           |  191       | 6778.76     | 0.49      | 0.45   |
|js             |  7900      | 275348.88   | 20.33     | 18.32  |  
|jshintrc       |  27        | 522.00      | 0.07      | 0.03   |
|json           |  224       | 5203.92     | 0.58      | 0.35   |
|lock           |  68        | 2160.64     | 0.17      | 0.14   |
|md             |  543       | 22097.92    | 1.40      | 1.47   |

5. Ao final da execução ele gera a quantidade total de arquivos capturados no terminal
6. Ao final da execução ele gera a informação de (processo terminado) no terminal
