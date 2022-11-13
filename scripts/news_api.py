import json
import requests
import yfinance as yf

        
msft = yf.Ticker("MSFT")
print(msft.news)

"""
fields = {
    "apiKey" : "da505f54ccb84881b5bbd7c9839c0a47",
    "country" : "us",
    "category" : "business",
    "q" : "HORIZON CORPORATION"
}
response = requests.get('https://newsapi.org/v2/top-headlines', params=fields)

print("Status Code", response.status_code)
print("JSON Response ", response.json())
"""