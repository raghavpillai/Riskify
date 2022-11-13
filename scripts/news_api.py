import json
import requests
import yfinance as yf
import random

def get_news_articles(holdings_arr):
    if len(holdings_arr) > 10:
        holdings_arr = holdings_arr[:10]
    
    ret = []
    ticker_arr = [yf.Ticker(ticker).news for ticker in holdings_arr]

    for ticker in ticker_arr:
        ret.extend(ticker)
    random.shuffle(ret)

    return ret[0:min(10,len(ret))]

# print(json.dumps(get_news_articles(['voo', 'vea', 'apple'])))