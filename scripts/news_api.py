import json
import requests
import yfinance as yf
import random
import math

def get_news_articles(holdings_arr):
    if len(holdings_arr) > 10:
        holdings_arr = holdings_arr[:10]
    
    ret = []
    ticker_arr = [yf.Ticker(ticker).news for ticker in holdings_arr]
    ticker_arr.sort(key=lambda x: len(x))
    length = int(10 / len(holdings_arr))

    for ticker in ticker_arr:
        ret.extend(ticker[0:min(len(ticker), length)])

    i = len(ticker_arr) - 1
    while i >= 0 and len(ret) < 10:
        if(len(ticker) < length):
            continue
        ret.extend(ticker[length:])

    random.shuffle(ret)

    return ret[0:min(10,len(ret))]

print(json.dumps(get_news_articles(['voo', 'vea', 'apple'])))