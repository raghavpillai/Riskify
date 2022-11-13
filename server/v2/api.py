import json
import os
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

historical_data = {}

file_dir = os.path.dirname(os.path.realpath('__file__'))

@app.get("/historical/<string:ticker>")
def get_historical_data(ticker):
  file_name = os.path.join(file_dir, '../../data/same.txt')
  f = open(f'{ticker.lower()}_.json')

  # returns JSON object as a dictionary
  data = json.load(f)

  # Iterating through the json
  # list
  for i in data['emp_details']:
      print(i)

  # Closing file
  f.close()

    with open(f"data/market/{ticker.lower()}_historical_data.json", "r") as f:
        historical_data = json.load(f)
    return jsonify(historical_data)


# @app.post("/item")
# def create_item():
#     request_data = request.get_json()
#     new_item_id = uuid.uuid4().hex
#     new_item = {
#         "name": request_data["name"],
#         "price": request_data["price"],
#         "store_id": request_data["store_id"],
#     }
#     items[new_item_id] = new_item
#     return new_item


# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}


# @app.get("/store/<string:id>")
# def get_store(id):
#     try:
#         # Here you might also want to add the items in this store
#         # We'll do that later on in the course
#         return stores[id]
#     except KeyError:
#         return {"message": "Store not found"}, 404


# @app.post("/store")
# def create_store():
#     request_data = request.get_json()
#     new_store_id = uuid.uuid4().hex
#     new_store = {"id": new_store_id, "name": request_data["name"]}
#     stores[new_store_id] = new_store
#     return new_store, 201


# @app.get("/store")
# def get_stores():
#     return {"stores": list(stores.values())}
