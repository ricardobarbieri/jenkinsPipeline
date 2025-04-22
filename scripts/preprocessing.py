import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

# Cria a pasta 'data/' se não existir
os.makedirs("data", exist_ok=True)

# Pré-processamento com tratamento de erro
try:
    if not os.path.exists("data/raw_data.csv"):
        raise FileNotFoundError("Arquivo 'raw_data.csv' não encontrado.")
    
    data = pd.read_csv("data/raw_data.csv")
    data = data.dropna()  # Remove valores nulos
    if "species" not in data.columns:
        raise ValueError("Coluna 'species' não encontrada nos dados brutos.")
    
    label_encoder = LabelEncoder()
    data["species"] = label_encoder.fit_transform(data["species"])
    data.rename(columns={"species": "target"}, inplace=True)  # Renomeia para 'target'
    data.to_csv("data/processed_data.csv", index=False)
    print("Dados pré-processados com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: {e}")
    exit(1)
except ValueError as e:
    print(f"Erro: {e}")
    exit(1)
except Exception as e:
    print(f"Erro inesperado: {e}")
    exit(1)