from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle
import os

# Verifica se os arquivos existem
try:
    os.makedirs("models", exist_ok=True)
    if not os.path.exists("data/processed_data.csv"):
        raise FileNotFoundError("Arquivo 'processed_data.csv' não encontrado.")
    
    # Carrega dados process    data = pd.read_csv("data/processed_data.csv")
    if "target" not in data.columns:
        raise ValueError("Coluna 'target' não encontrada nos dados processados.")
    
    X = data.drop("target", axis=1)
    y = data["target"]

    # Treina modelo
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    # Salva modelo
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Modelo treinado com sucesso.")

except FileNotFoundError as e:
    print(f"Erro: {e}")
    exit(1)
except ValueError as e:
    print(f"Erro: {e}")
    exit(1)
except Exception as e:
    print(f"Erro inesperado: {e}")
    exit(1)