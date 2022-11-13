import json
import requests
import random
import os
from sqlitedict import SqliteDict
from modules.model import get_points
from modules.news_articles import get_news_articles

# db = SqliteDict("risk_analysis.sqlite")

file_dir = os.path.dirname(os.path.realpath("__file__"))

ticker_categories = {
    "gold": ["SGOL"],
    "real_estate": ["VNQ"],
    "stocks": ["IVOV", "VEA", "VIOV", "VOO", "VT", "VTI", "VWO"],
    "treasury": {"bonds": ["SCHP", "VGLT"], "notes": ["VGIT", "VGSH", "VTIP"]},
}

top_holdings = {
    "ultra_aggressive": [
        ["Vanguard 500 Index Fund ETF", "0.25"],
        ["Vanguard Developed Markets Index Fund ETF", "0.25"],
        ["Vanguard Emerging Markets Stock Index Fund ETF", "0.25"],
        ["Vanguard S&P Mid-Cap 400 Value Index Fund ETF", "0.10"],
        ["Vanguard S&P Small Cap 600 Value ETF", "0.10"],
        ["Vanguard Real Estate Index Fund ETF", "0.05"],
    ],
    "moderately_aggressive": [
        ["Vanguard 500 Index Fund ETF", "0.25"],
        ["Vanguard Developed Markets Index Fund ETF", "0.15"],
        ["Vanguard Emerging Markets Stock Index Fund ETF", "0.15"],
        ["Vanguard S&P Mid-Cap 400 Value Index Fund ETF", "0.10"],
        ["Vanguard S&P Small Cap 600 Value ETF", "0.10"],
        ["Vanguard Real Estate Index Fund ETF", "0.05"],
        ["Vanguard Long-Term Treasury Index Fund ETF", "0.2"],
    ],
    "moderate": [
        ["Vanguard 500 Index Fund ETF", "0.15"],
        ["Vanguard Developed Markets Index Fund ETF", "0.15"],
        ["Vanguard Emerging Markets Stock Index Fund ETF", "0.15"],
        ["Vanguard S&P Mid-Cap 400 Value Index Fund ETF", "0.1"],
        ["Vanguard S&P Small Cap 600 Value ETF", "0.1"],
        ["Vanguard Real Estate Index Fund ETF", "0.05"],
        ["Vanguard Long-Term Treasury Index Fund ETF", "0.2"],
        ["Vanguard Intermediate-Term Treasury Index Fd ETF", "0.1"],
    ],
    "moderately_conservative": [
        ["Vanguard 500 Index Fund ETF", "0.15"],
        ["Vanguard Developed Markets Index Fund ETF", "0.15"],
        ["Vanguard Emerging Markets Stock Index Fund ETF", "0.15"],
        ["Vanguard S&P Mid-Cap 400 Value Index Fund ETF", "0.05"],
        ["Vanguard S&P Small Cap 600 Value ETF", "0.05"],
        ["Vanguard Real Estate Index Fund ETF", "0.05"],
        ["Vanguard Long-Term Treasury Index Fund ETF", "0.2"],
        ["Vanguard Intermediate-Term Treasury Index Fd ETF", "0.2"],
    ],
    "conservative": [
        ["Vanguard Total Stock Market Index Fund ETF", "0.1"],
        ["Vanguard Developed Markets Index Fund ETF", "0.1"],
        ["Vanguard Emerging Markets Stock Index Fund ETF", "0.1"],
        ["Vanguard S&P Small Cap 600 Value ETF", "0.05"],
        ["Vanguard Real Estate Index Fund ETF", "0.05"],
        ["Vanguard Intermediate-Term Treasury Index Fd ETF", "0.4"],
        [
            "Schwab US TIPS ETF (Treasury Inflation-Protected Securities)",
            "0.2",
        ],
    ],
    "ultra_conservative": [
        ["Vanguard Total World Stock Index Fund ETF", "0.1"],
        ["Vanguard S&P Small Cap 600 Value ETF", "0.03"],
        ["Vanguard Real Estate Index Fund ETF", "0.02"],
        ["abrdn Physical Gold Shares ETF", "0.05"],
        ["Vanguard Intermediate-Term Treasury Index Fd ETF", "0.2"],
        ["Vanguard Short-Term Treasury Index Fund ETF", "0.4"],
        ["Vanguard Short-Term Inflation-Protected Sec Idx ETF", "0.2"],
    ],
}

ticker_folders = {
    "sgol": "gold",
    "vnq": "real_estate",
    "ivov": "stocks",
    "vea": "stocks",
    "viov": "stocks",
    "voo": "stocks",
    "vt": "stocks",
    "vti": "stocks",
    "vwo": "stocks",
    "schp": "treasury/bond",
    "vglt": "treasury/bond",
    "vgit": "treasury/notes",
    "vgsh": "treasury/notes",
    "vtip": "treasury/notes",
}


def process_file(ticker_name):
    # if db.get(f"{ticker_name}_file"):
    # print("CACHE ACCESSED FOR FILE OPEN")
    # return db[f"{ticker_name}_file"]
    values = []
    file = open(
        os.path.join(
            file_dir,
            f"data_new/{ticker_folders[ticker_name]}/{ticker_name}_historical_data.json",
        )
    )
    data = json.load(file)
    for i in data:
        values.append(float(data[i]["Close"]))
    file.close()
    # db[f"{ticker_name}_file"] = values
    return values


def get_risk_for_portfolio_helper(capital, portfolio_type, payload=None):
    if portfolio_type == "ultra_aggressive":
        return {
            "VOO": capital * 0.25,
            "VEA": capital * 0.25,
            "VWO": capital * 0.25,
            "IVOV": capital * 0.1,
            "VIOV": capital * 0.1,
            "VNQ": capital * 0.05,
        }
    elif portfolio_type == "aggressive":
        return {
            "VOO": capital * 0.25,
            "VEA": capital * 0.2,
            "VWO": capital * 0.2,
            "IVOV": capital * 0.1,
            "VIOV": capital * 0.1,
            "VNQ": capital * 0.05,
            "VGLT": capital * 0.1,
        }
    elif portfolio_type == "moderately_aggressive":
        return {
            "VOO": capital * 0.25,
            "VEA": capital * 0.15,
            "VWO": capital * 0.15,
            "IVOV": capital * 0.1,
            "VIOV": capital * 0.1,
            "VNQ": capital * 0.05,
            "VGLT": capital * 0.2,
        }
    elif portfolio_type == "moderate":
        return {
            "VOO": capital * 0.15,
            "VEA": capital * 0.15,
            "VWO": capital * 0.15,
            "IVOV": capital * 0.1,
            "VIOV": capital * 0.1,
            "VNQ": capital * 0.05,
            "VGLT": capital * 0.2,
            "VGIT": capital * 0.1,
        }
    elif portfolio_type == "moderately_conservative":
        return {
            "VOO": capital * 0.15,
            "VEA": capital * 0.15,
            "VWO": capital * 0.15,
            "IVOV": capital * 0.05,
            "VIOV": capital * 0.05,
            "VNQ": capital * 0.05,
            "VGLT": capital * 0.2,
            "VGIT": capital * 0.2,
        }
    elif portfolio_type == "conservative":
        return {
            "VTI": capital * 0.1,
            "VEA": capital * 0.1,
            "VWO": capital * 0.1,
            "VIOV": capital * 0.05,
            "VNQ": capital * 0.05,
            "VGIT": capital * 0.4,
            "SCHP": capital * 0.2,
        }
    else:  # portfolio_type == "ultra_conservative":  # ultra_conservative
        return {
            "VT": capital * 0.1,
            "VIOV": capital * 0.03,
            "VNQ": capital * 0.02,
            "SGOL": capital * 0.05,
            "VGIT": capital * 0.2,
            "VGSH": capital * 0.4,
            "VTIP": capital * 0.2,
        }


def future_portfolio_values(capital, portfolio_type, payload=None):
    return get_portfolio_value_x_year(
        get_risk_for_portfolio_helper(capital, portfolio_type, payload)
    )


def get_risk_for_portfolio(capital, portfolio_type, payload=None):
    # if db.get(f"{portfolio_type}_{capital}"):
    # print("CACHE ACCESSED FOR RISK_ANALYSIS")
    # return db[f"{portfolio_type}_{capital}"]

    risks = future_portfolio_values(capital, portfolio_type, payload)
    fields = {
        "alpha": 0.05,
        "portfolios": [{"portfolioValues": risks["total_graph"]}],
    }
    response = requests.post(
        "https://api.portfoliooptimizer.io/v1/portfolio/analysis/conditional-value-at-risk",
        json=fields,
    )
    risk = 0
    try:
        risk = float(
            response.json()["portfolios"][0]["portfolioConditionalValueAtRisk"]
        )
    except:
        print("API CALLS HIT")
        print(response.json())
        risk = 0.026584279145694695

    #db[f"{portfolio_type}_{capital}"] = {portfolio_type: risk}
    #db.commit()
    obj = {
        "ultra_aggressive": 0.7,
        "moderately_aggressive": 0.55,
        "moderate": 0.4,
        "moderately_conservative": 0.325,
        "conservative": 0.1,
        "ultra_conservative": 0,
    }
    
    score = risk + obj[portfolio_type]
    return {portfolio_type: score}


def get_return_for_portfolio(capital, portfolio_type):

    # if db.get(f"{portfolio_type}_{capital}_return"):
    #    print("CACHE ACCESSED FOR RETURN_PORTFOLIO")
    #    return db[f"{portfolio_type}_{capital}_return"]

    returns = future_portfolio_values(capital, portfolio_type)
    fields = {
        "portfolios": [{"portfolioValues": returns}],
    }
    response = requests.post(
        "https://api.portfoliooptimizer.io/v1/portfolio/analysis/returns/average",
        json=fields,
    )
    arithmetic_return = 0
    try:
        arithmetic_return = float(
            response.json()["portfolios"][0]["portfolioAverageReturn"]
        )
    except:
        print("API CALLS HIT")
        arithmetic_return = 0.026584279145694695

    return {portfolio_type: arithmetic_return}


def get_portfolio_value_x_year(portfolio):
    file = open(os.path.join(file_dir, f"new_monte_carlo.json"))
    data = json.load(file)
    projected_portfolio_value = [0] * 26

    ind_graphs = {}
    p_v = 0
    for ticker, value in portfolio.items():
        ticker = ticker.lower()
        ind_graphs[ticker] = []
        # years 0-25 of the ticker

        for i in range(0, len(data[ticker])):
            ratio_change = random.uniform(1.05, 0.98)
            ratio_change = sorted((0.98, ratio_change, 1.05))[1]
            if i == 0:
                p_v = value
            # add this tickers new value to that year of the projected portfolio
            ind_graphs[ticker].append(value)
            projected_portfolio_value[i] += value
            value = round(value * ratio_change, 2)

        ind_graphs[ticker][0] = p_v
        get_points(ind_graphs[ticker])

    file.close()
    # points = get_points(projected_portfolio_value)
    # print(points)
    projected_portfolio_value.pop(1)
    return {"total_graph": projected_portfolio_value, "ind_graphs": ind_graphs}


def return_analyzed_data(capital, has_portfolio, portfolio_type, payload=None):
    balances = {}
    portfolio = get_risk_for_portfolio_helper(capital, portfolio_type, payload)
    keys = portfolio.keys()
    articles = get_news_articles(list(keys))

    if has_portfolio == "true":
        # balances = payload["balances"]
        capital_funds = capital * (int(payload["capitalWeight"]) * 0.01)
        balances["stocks"] = capital_funds * (int(payload["stocks"]) * 0.01)
        balances["bonds_and_notes"] = capital_funds * (
            int(payload["bonds_and_notes"]) * 0.01
        )
        balances["realEstate"] = capital_funds * (
            int(payload["realEstate"]) * 0.01
        )
        balances["commodities"] = capital_funds * (
            int(payload["commodities"]) * 0.01
        )
    return {
        "risk": get_risk_for_portfolio(capital, portfolio_type, payload),
        "future_points": get_portfolio_value_x_year(
            get_risk_for_portfolio_helper(capital, portfolio_type, payload)
        ),
        "articles": articles,
        "balancing": balances,
    }
