import json
import requests
import os

goal_dir = os.path.join(os.getcwd(), "data/market/")


tot_values = []
for filename in os.listdir(goal_dir):
    f = os.path.join(goal_dir, filename)
    if os.path.isfile(f):
        values = []
        file = open(f)
        data = json.load(file)
        for i in data:
            values.append(data[i]["Close"])
        tot_values.append(values)
        file.close()
        
for table in tot_values:
    headers = {"Content-type": "application/json"}
    fields = {
        "alpha": 0.05,
        "portfolios": [
            {
                "portfolioValues": table
            }
        ]
    }
    response = requests.post('https://api.portfoliooptimizer.io/v1/portfolio/analysis/conditional-value-at-risk', json=fields)

    print("Status Code", response.status_code)
    print("JSON Response ", response.json())