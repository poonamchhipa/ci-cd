from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Flask is running inside Docker."

@app.route('/data')
def get_data():
    try:
        df = pd.read_csv("placement.csv")
        return df.head().to_json(orient="records")
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
