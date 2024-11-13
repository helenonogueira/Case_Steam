# **Case Técnico: Extração e Análise de Dados da Steam**

Este projeto visa realizar a extração de dados de ofertas de jogos do site SteamDB Sales, armazená-los no Google BigQuery e exportá-los 
para o Google Sheets para visualização e análise. A partir do Google Sheets, foram gerados gráficos para identificar tendências e insights 
com base nas variáveis extraídas.

## **Descrição do Projeto**
O objetivo principal foi construir uma automação que extrai informações relevantes de jogos, como nome, preço, data de lançamento, avaliação e 
desconto, para análise e consulta. O projeto incluiu a raspagem de dados, o armazenamento estruturado no Google BigQuery e a exportação para o 
Google Sheets, onde foram criados gráficos para visualizações.

### **Tecnologias Utilizadas**
* Python: Para desenvolver o script de automação e raspagem de dados com Selenium.
* Selenium: Para realizar a extração dos dados da web (web scraping) no site SteamDB.
* Google BigQuery: Para armazenar e organizar os dados extraídos.
* Google Sheets: Para visualizar, analisar e compartilhar os dados por meio de gráficos.
* Pandas: Para organizar os dados raspados e facilitar o carregamento no BigQuery.

## **Estrutura do Projeto**
O repositório inclui os seguintes arquivos:
* script_steam.py: Script Python principal que realiza a raspagem dos dados, estrutura as informações e carrega no BigQuery.
* requirements.txt: Arquivo de dependências para instalar as bibliotecas necessárias, como Selenium e Google BigQuery.
* README.md: Documento de descrição do projeto e instruções de uso.


### **1. Raspagem de Dados com Selenium**
Para a extração dos dados:
Utilizamos o Selenium para abrir o site SteamDB Sales e navegar pelas páginas de descontos.

### **2. O script coleta os dados relevantes, incluindo:**
Nome do jogo
Data de lançamento
Avaliação do jogo
Desconto aplicado
Preço com desconto
Os dados são armazenados em listas e, ao final do processo, são organizados em um DataFrame usando a biblioteca Pandas.

![Tabela_completa](https://github.com/user-attachments/assets/8cc9de30-0b05-4339-a306-287ce3738b51)

### **3. Armazenamento no Google BigQuery**
Após a raspagem, os dados são carregados no Google BigQuery:
Configuramos o cliente BigQuery no script Python para realizar a conexão com o dataset específico.
Criamos o dataset e a tabela dentro do BigQuery, caso ainda não existam, e configuramos para sobrescrever dados antigos ao carregar novos.
Realizamos o upload dos dados do DataFrame diretamente para o BigQuery.

![big_query](https://github.com/user-attachments/assets/a78c06d2-f512-4688-b774-da89f9f7d10a)


### **4. Exportação e Análise no Google Sheets**
Para facilitar a análise:
Conectamos a tabela BigQuery ao Google Sheets através do conector BigQuery do próprio Google Sheets.
Com os dados no Google Sheets, configuramos gráficos para analisar as relações entre variáveis, incluindo:
Desconto por data de lançamento
Distribuição de descontos

![Tabela_500_views](https://github.com/user-attachments/assets/79aa1988-30d3-42e8-ab73-1419a333bec6)

![analises](https://github.com/user-attachments/assets/d8966190-481f-4cfc-a084-c60e4f14db83)




**Instale as dependências:**

pip install -r requirements.txt


**Configure seu arquivo de credenciais do Google BigQuery no caminho correto e execute o script:**
python steam_scraping.py


**Google Sheets e Link do Repositório**

Link do Repositório GitHub: [Link do Repositório](https://github.com/helenonogueira/case_steam.git)

Link do Google Sheets: [Planilha de Análise de Dados SteamDB](https://docs.google.com/spreadsheets/d/1OL7HX-NbdevwIRSJ8n2nk94GRkTHzhbmtWrpJB-4HzM/edit?usp=sharing)
