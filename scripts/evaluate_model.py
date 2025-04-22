from sklearn.metrics import accuracy_score
import pandas as pd
import pickle
import os

# Verifica se os arquivos existem
try:
    if not os.path.exists("data/processed_data.csv"):
        raise FileNotFoundError("Arquivo 'processed_data.csv' não encontrado.")
    if not os.path.exists("models/model.pkl"):
        raise FileNotFoundError("Modelo 'model.pkl' não encontrado.")

    # Carrega dados e modelo
    data = pd.read_csv("data/processed_data.csv")
    if "target" not in data.columns:
        raise ValueError("Coluna 'target' não encontrada nos dados processados.")
    X = data.drop("target", axis=1)
    y = data["target"]
    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)

    # Avalia modelo
    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    print(f"Acurácia do modelo: {accuracy:.2f}")

except FileNotFoundError as e:
    print(f"Erro: {e}")
    exit(1)
except ValueError as e:
    print(f"Erro: {e}")
    exit(1)
except Exception as e:
    print(f"Erro inesperado: {e}")
    exit(1)