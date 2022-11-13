import json
import os
from flask import Flask, request
from flask import jsonify
from modules.risk_analysis import (
    get_risk_for_portfolio,
    get_return_for_portfolio,
)

app = Flask(__name__)

historical_data = {}
predictions_data_cache = {}
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
    body = request.json
    if "ticker" not in body:
        return jsonify({"msg": "Ticker must be passed."}), 400

    ticker = body["ticker"].lower()
    if predictions_data_cache and ticker in predictions_data_cache:
        return jsonify(predictions_data_cache[ticker]), 200

    data_file = os.path.join(file_dir, f"../../data/new_monte_carlo.json")
    with open(data_file, "r") as f:
        predictions_data = json.load(f)
        return jsonify(predictions_data[ticker]), 200


@app.get("/risk")
def get_risk_analysis():
    body = request.json
    if "portfolio" not in body or "capital" not in body:
        return (
            jsonify({"msg": "Portfolio type or capital must be passed."}),
            400,
        )
    type = body["portfolio"]
    capital = body["capital"]
    return jsonify(get_risk_for_portfolio(capital, type)), 200


@app.get("/return")
def get_return_analysis():
    body = request.json
    if "portfolio" not in body or "capital" not in body:
        return (
            jsonify({"msg": "Portfolio type or capital must be passed."}),
            400,
        )
    type = body["portfolio"]
    capital = body["capital"]
    return jsonify(get_return_for_portfolio(capital, type)), 200


app.run(debug=True)
