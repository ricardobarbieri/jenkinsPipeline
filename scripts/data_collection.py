import pandas as pd
import os
import requests

# Cria a pasta 'data/' se não existir
os.makedirs("data", exist_ok=True)

# Coleta de dados com tratamento de erro
try:
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Levanta exceção para erros HTTP
    data = pd.read_csv(url)
    data.to_csv("data/raw_data.csv", index=False)
    print("Dados coletados com sucesso.")
except requests.RequestException as e:
    print(f"Erro ao baixar os dados: {e}")
    exit(1)
except pd.errors.EmptyDataError:
    print("Erro: O arquivo CSV está vazio.")
    exit(1)
except Exception as e:
    print(f"Erro inesperado: {e}")
    exit(1)