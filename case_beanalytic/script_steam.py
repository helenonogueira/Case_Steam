from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from google.cloud import bigquery
import pandas as pd
import time

# Webdriver para busca
driver = webdriver.Chrome()
driver.get("https://steamdb.info/sales/")
time.sleep(5)

names = []
discounts = []
prices = []
ratings = []
release_dates = []

while True:
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr.app")))
    rows = driver.find_elements(By.CSS_SELECTOR, "tr.app")

    for row in rows:
        name = row.find_element(By.CSS_SELECTOR, "a.b").text.strip()
        discount = row.find_elements(By.CSS_SELECTOR, "td.dt-type-numeric")[1].text.strip()
        price = row.find_elements(By.CSS_SELECTOR, "td.dt-type-numeric")[2].text.strip()
        rating = row.find_elements(By.CSS_SELECTOR, "td.dt-type-numeric")[3].text.strip()
        release_date = row.find_elements(By.CSS_SELECTOR, "td.dt-type-numeric")[4].text.strip()

        names.append(name)
        discounts.append(discount)
        prices.append(price)
        ratings.append(rating)
        release_dates.append(release_date)

    data = {
        "Game Name": names,
        "Discount": discounts,
        "Price": prices,
        "Rating": ratings,
        "Release Date": release_dates
    }

    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.dt-paging-button.next"))
        )
        if "disabled" in next_button.get_attribute("class"):
            print("Fim da busca")
            break
        next_button.click()
        time.sleep(5)
    except TimeoutException:
        print("Não foram encontradas páginas seguintes")
        break

driver.quit()

# Gerando DataFrame
df = pd.DataFrame(data)
df['row_id'] = df.index + 1
reorder = ['row_id', 'Game Name', 'Discount', 'Price', 'Rating', 'Release Date']
df = df[reorder]

# Configuração do BigQuery
client = bigquery.Client.from_service_account_json('C:\\Users\\Heleno\\Documents\\Cases\\case_beanalytic\\key_acess\\casebeanalytic2024-1dc659a0400e.json')

# Definição do ID do dataset e da tabela
dataset_id = "casebeanalytic2024.steam_db"
table_id = f"{dataset_id}.steam_sales"

# Verificação e criação do dataset se não existir
dataset = bigquery.Dataset(dataset_id)
dataset.location = "US"
client.create_dataset(dataset, exists_ok=True)

# Configuração e carregamento dos dados para o BigQuery
job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
job.result()  # Aguarda a conclusão do job

print("Dados carregados com sucesso no BigQuery.")
