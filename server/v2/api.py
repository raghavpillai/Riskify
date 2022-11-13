import json
import os
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

historical_data = {}
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


@app.get("/historical/<string:category>/<string:ticker>")
def get_historical_data(category, ticker):
    if category not in ticker_categories:
        return jsonify({"msg": "Invalid category passed."}), 400
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


app.run(debug=True)
