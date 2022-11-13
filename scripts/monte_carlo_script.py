import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_pred_var(df, number_of_years, num_future):
    total_growth = (df.iloc[-1]['val'] / df.iloc[0]['val'])
    cagr = total_growth ** (1/number_of_years) - 1
    std_dev = df['val'].pct_change().std()
    number_of_trading_days = num_future
    std_dev = std_dev * math.sqrt(number_of_trading_days)

  
    number_of_trials = 3000
    closing_prices = []
    for i in range(number_of_trials):
        # each single trial
        daily_return_percentages = np.random.normal(cagr/number_of_trading_days, std_dev/math.sqrt(number_of_trading_days),number_of_trading_days)+1
        price_series = [df.iloc[-1]['val']]
    
        for j in daily_return_percentages:
            price_series.append(price_series[-1] * j)
        
        closing_prices.append(price_series[-1])
    
    mean_end_price = round(np.mean(closing_prices),2)
    top_ten = np.percentile(closing_prices,100-10)
    bottom_ten = np.percentile(closing_prices,10)
    
    return {"bottom_ten": bottom_ten, "mean_price": round(np.mean(closing_prices),2), "top_ten": top_ten} # df.iloc[-1]['val']

# df = pd.read_csv('blla.csv', names=['date', 'val'])
# print(get_pred_var(df, 18829 / 365.0, 25 * 52))

from datetime import datetime

for name in ['ivov', 'schp', 'sgol', 'vea', 'vgit', 'vglt', 'vgsh', 'viov', 'vnq', 'voo', 'vt', 'vti', 'vtip', 'vwo']:
    path = name + '_historical_data.csv'
    df = pd.read_csv(path)

    def toDate(dateStr):
        return datetime.strptime(dateStr, '%Y-%m-%d')
    num_years = (toDate(df.iloc[-1]['Date'].split(" ")[0]) - toDate(df.iloc[0]['Date'].split(" ")[0])).days / 365.0

    print("\"" + name + "\"" + ": ")
    print("{")
    for year in range(5, 26, 5):
        num_future = year * 252
        df.rename(columns={'Close': 'val'}, inplace=True)
        print("\"" + str(year) + "\"" + ":", end='')
        # print(df.head(), num_years, num_future)
        print(str(get_pred_var(df, num_years, num_future)).replace("\'", "\"") + (',' if year < 25 else ''))
    print("},")
    # print("------")

