import json
import requests


#Opening JSON file
f = open('historical.json')
  
data = json.load(f)

values = []
for i in data['data']:
    values.append(i['close'])
  
#Closing file
f.close()

headers = {"Content-type": "application/json"}
fields = {
    "alpha": 0.05,
    "portfolios": [
        {
            "portfolioValues": values
        }
    ]
}

response = requests.post('https://api.portfoliooptimizer.io/v1/portfolio/analysis/conditional-value-at-risk', json=fields)

print("Status Code", response.status_code)
print("JSON Response ", response.json())