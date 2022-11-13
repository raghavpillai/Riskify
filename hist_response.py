import json
import requests
import os

def get_risk_from_data(folder_name):
    goal_dir = os.path.join(os.getcwd(), f"data/{folder_name}/")

    tot_values = []
    for filename in os.listdir(goal_dir):
        f = os.path.join(goal_dir, filename)
        if os.path.isfile(f):
            values = []
            file = open(f)
            data = json.load(file)
            for i in data:
                values.append(float(data[i]["Close"]))
            tot_values.append(values)
            file.close()

    risks = 0
    for table in tot_values:
        headers = {"Content-type": "application/json"}
        fields = {
            "alpha": 0.05,
            "portfolios": [
                {
                    "portfolioValues": table[-500:]
                }
            ]
        }
        response = requests.post('https://api.portfoliooptimizer.io/v1/portfolio/analysis/conditional-value-at-risk', json=fields)

        risk = 0
        try:
            risk = float(response.json()['portfolios'][0]['portfolioConditionalValueAtRisk'])
        except:
            risk = 0.026584279145694695
        risks += risk
    
    return risks

risks = get_risk_from_data("market")
print(risks)