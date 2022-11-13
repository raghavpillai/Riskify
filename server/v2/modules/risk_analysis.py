import json
import requests
from threading import Thread
import os

risks = {}


def process_file(file_name):
    values = []
    file = open(file_name)
    data = json.load(file)
    for i in data:
        values.append(float(data[i]["Close"]))
    file.close()
    return values


def get_risk_from_data(folder_name):
    goal_dir = os.path.join(os.getcwd(), f"data/{folder_name}/")

    tot_values = []
    for filename in os.listdir(goal_dir):
        f = os.path.join(goal_dir, filename)
        if os.path.isfile(f):
            table = process_file(f)
            tot_values.append(table)

    risks = 0
    for table in tot_values:
        fields = {
            "alpha": 0.05,
            "portfolios": [{"portfolioValues": table[-500:]}],
        }
        response = requests.post(
            "https://api.portfoliooptimizer.io/v1/portfolio/analysis/conditional-value-at-risk",
            json=fields,
        )

        risk = 0
        try:
            risk = float(
                response.json()["portfolios"][0][
                    "portfolioConditionalValueAtRisk"
                ]
            )
        except:
            risk = 0.026584279145694695
        risks += risk

    avg_risk = risks / len(tot_values)
    risks[folder_name] = avg_risk

    return avg_risk


risks = get_risk_from_data("stocks")
print(risks)
