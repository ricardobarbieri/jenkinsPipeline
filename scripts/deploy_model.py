from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Verifica e carrega o modelo
try:
    os.makedirs("models", exist_ok=True)
    if not os.path.exists("models/model.pkl"):
        raise FileNotFoundError("Modelo 'model.pkl' não encontrado.")
    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError as e:
    print(f"Erro: {e}")
    exit(1)
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    exit(1)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        if not isinstance(data.get("features"), list) or len(data["features"]) != 4:
            return jsonify({"error": "Features deve ser uma lista com 4 números."}), 400
        prediction = model.predict([data["features"]])
        return jsonify({"prediction": int(prediction[0])})
    except KeyError:
        return jsonify({"error": "Chave 'features' não encontrada no JSON."}), 400
    except Exception as e:
        return jsonify({"error": f"Erro na predição: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)