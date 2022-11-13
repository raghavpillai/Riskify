import json
import os
from flask import Flask, request
from flask import jsonify
from modules.monte_carlo_script import get_monte_carlo_preds

app = Flask(__name__)

historical_data = {}
predictions_data = get_monte_carlo_preds()
print(predictions_data)
ticker_categories = {
    "gold": ["SGOL"],
    "real_estate": ["VNQ"],
    "stocks": ["IVOV", "VEA", "VIOV", "VOO", "VT", "VTI", "VWO"],
    "treasury": {"bond": ["SCHP", "VGLT"], "notes": ["VGIT", "VGSH", "VTIP"]},
}

file_dir = os.path.dirname(os.path.realpath("__file__"))


@app.get("/")
def index():
    return jsonify({"msg": "Hello World"})


@app.get("/historical")
def get_historical_data():
    body = request.json
    if "category" not in body or "ticker" not in body:
        return jsonify({"msg": "Category and ticker must be passed."}), 400

    category = body["category"]
    if category not in ticker_categories:
        return jsonify({"msg": "Invalid category passed."}), 400
    ticker = body["ticker"]
    if ticker in historical_data:
        return jsonify(historical_data[ticker]), 200

    if "_" in category:
        category = category.replace("_", "/")

    data_file = os.path.join(
        file_dir, f"../../data/{category}/{ticker}_historical_data.json"
    )
    with open(data_file, "r") as f:
        historical_data[ticker] = json.load(f)
        return jsonify(historical_data[ticker]), 200


@app.get("/prediction")
def get_prediction_data():
    print(predictions_data)
    body = request.json
    if "ticker" not in body:
        return jsonify({"msg": "Ticker must be passed."}), 400

    ticker = body["ticker"].lower()
    if ticker not in predictions_data:
        return jsonify({"msg": "Ticker not found."}), 400

    return jsonify(predictions_data[ticker]), 200


app.run(debug=True)
