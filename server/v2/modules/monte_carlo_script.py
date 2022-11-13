import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json
import os
from datetime import datetime
from sqlitedict import SqliteDict
db = SqliteDict("risk_analysis.sqlite")


def get_pred_var(df, number_of_years, num_future):
    total_growth = df.iloc[-1]["val"] / df.iloc[0]["val"]
    cagr = total_growth ** (1 / number_of_years) - 1
    std_dev = df["val"].pct_change().std()
    number_of_trading_days = num_future
    std_dev = std_dev * math.sqrt(number_of_trading_days)

    number_of_trials = 3000
    closing_prices = []
    for i in range(number_of_trials):
        # each single trial
        daily_return_percentages = (
            np.random.normal(
                cagr / number_of_trading_days,
                std_dev / math.sqrt(number_of_trading_days),
                number_of_trading_days,
            )
            + 1
        )
        price_series = [df.iloc[-1]["val"]]

        for j in daily_return_percentages:
            price_series.append(price_series[-1] * j)

        closing_prices.append(price_series[-1])

    mean_end_price = round(np.mean(closing_prices), 2)
    top_ten = np.percentile(closing_prices, 100 - 10)
    bottom_ten = np.percentile(closing_prices, 10)

    print(bottom_ten, round(np.mean(closing_prices), 2), top_ten)
    return {
        "bottom_ten": bottom_ten,
        "mean_price": round(np.mean(closing_prices), 2),
        "top_ten": top_ten,
    }  # df.iloc[-1]['val']


# returns map in this format:
"""
{'ivov':
    {'1': {'bottom_ten': 139.31101597858049, 'mean_price': 184.59, 'top_ten': 233.52857026504262},
    '2': {'bottom_ten': 123.40489545790815, 'mean_price': 186.39, 'top_ten': 259.58008467202063}},
'schp':
    {'1': {'bottom_ten': 50.279066263436796, 'mean_price': 54.09, 'top_ten': 58.020346893310794},
    '2': {'bottom_ten': 48.689769580252886, 'mean_price': 54.1, 'top_ten': 59.667930565105394}
}
"""


def get_monte_carlo_preds():
    if db.get("carlo"):
        print("CACHE ACCESSED FOR RISK_ANALYSIS")
        return db["carlo"]

    goal_dir = os.path.join(os.getcwd(), "data_old/market/")

    ret = {}
    for filename in os.listdir(goal_dir):
        f = os.path.join(goal_dir, filename)
        key_str = filename.split("_")[0]
        print(key_str)
        ret[key_str] = {}
        if os.path.isfile(f):
            values = []
            file = open(f)
            data = json.load(file)
            for i in data:
                values.append(float(data[i]["Close"]))
            df = pd.DataFrame(data=values, columns=["val"])

            for i in range(1, 26):
                ret[key_str][str(i)] = get_pred_var(df, 10, 250 * i)
            file.close()

    db["carlo"] = ret
    db.commit()
    return ret
    