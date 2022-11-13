import json
import requests
import os
from sqlitedict import SqliteDict

db = SqliteDict("risk_analysis.sqlite")

file_dir = os.path.dirname(os.path.realpath("__file__"))

ticker_categories = {
    "gold": ["SGOL"],
    "real_estate": ["VNQ"],
    "stocks": ["IVOV", "VEA", "VIOV", "VOO", "VT", "VTI", "VWO"],
    "treasury": {"bonds": ["SCHP", "VGLT"], "notes": ["VGIT", "VGSH", "VTIP"]},
}

def process_file(file_name):
    values = []
    file = open(file_name)
    data = json.load(file)
    for i in data:
        values.append(float(data[i]["Close"]))
    file.close()
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
    elif portfolio_type == "ultra_conservative":  # ultra_conservative
        return {
            "VT": capital * 0.1,
            "VIOV": capital * 0.03,
            "VNQ": capital * 0.02,
            "SGOL": capital * 0.05,
            "VGIT": capital * 0.2,
            "VGSH": capital * 0.4,
            "VTIP": capital * 0.2,
        }
    else: # Custom payload 
        categories = {}
        for stock in ticker_categories["stocks"]:
            print(payload)
            print(payload["stocks"])
            categories[stock] = (payload["stocks"] * 0.01) * capital
            print(categories[stock])
        for stock in ticker_categories["treasury"]["bonds"]:
            categories[stock] = (payload["bonds_and_notes"] * 0.01) * capital
        for stock in ticker_categories["treasury"]["notes"]:
            categories[stock] = (payload["bonds_and_notes"] * 0.01) * capital
        #categories["capital"] = (payload["capitalWeight"] * 0.01) * capital
        for stock in ticker_categories["real_estate"]:
            categories[stock] = (payload["realEstate"] * 0.01) * capital
        for stock in ticker_categories["gold"]:
            categories[stock] = (payload["commodities"] * 0.01) * capital
        print(categories)
        return categories


def future_portfolio_values(capital, portfolio_type, payload=None):
    return get_portfolio_value_x_year(
        get_risk_for_portfolio_helper(capital, portfolio_type, payload)
    )


def get_risk_for_portfolio(capital, portfolio_type, payload=None):
    if db.get(f"{portfolio_type}_{capital}"):
        print("CACHE ACCESSED FOR RISK_ANALYSIS")
        return db[f"{portfolio_type}_{capital}"]

    risks = future_portfolio_values(capital, portfolio_type, payload)
    fields = {
        "alpha": 0.05,
        "portfolios": [{"portfolioValues": risks}],
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
        risk = 0.026584279145694695

    db[f"{portfolio_type}_{capital}"] = {portfolio_type: risk}
    db.commit()

    return {portfolio_type: risk}


def get_return_for_portfolio(capital, portfolio_type):
    if db.get(f"{portfolio_type}_{capital}_return"):
        print("CACHE ACCESSED FOR RETURN_PORTFOLIO")
        return db[f"{portfolio_type}_{capital}_return"]

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
        arithmetic_return = 0.026584279145694695

    db[f"{portfolio_type}_{capital}_return"] = {
        portfolio_type: arithmetic_return
    }
    db.commit()

    return {portfolio_type: arithmetic_return}


def get_portfolio_value_x_year(portfolio):
    file = open(os.path.join(file_dir, f"new_monte_carlo.json"))
    data = json.load(file)
    projected_portfolio_value = [0] * 26

    ind_graphs = {}
    for ticker, value in portfolio.items():
        ticker = ticker.lower()
        ind_graphs[ticker] = []
        # years 0-25 of the ticker
        for i in range(0, len(data[ticker])):
            # finding mean_price at that year
            mean_price = float(data[ticker][f"{i}"]["mean_price"])
            # ratio change of this ticker, (future / now)
            ratio_change = mean_price / float(
                data[ticker][f"{i - 1 if i > 0 else i}"]["mean_price"]
            )
            # add this tickers new value to that year of the projected portfolio
            ind_graphs[ticker].append(value * ratio_change)
            projected_portfolio_value[i] += value * ratio_change
    file.close()
    return {"total_graph": projected_portfolio_value, "ind_graphs": ind_graphs}


def return_analyzed_data(capital, portfolio_type, payload=None):
    balances = {}
    if portfolio_type == "true":
        capital_funds = (capital * payload["capitalWeight"] * 0.01)/4
        balances["stocks"] = (capital * 0.25) - (capital * payload["stocks"] * 0.01) - capital_funds
        balances["bonds_and_notes"] = (capital * 0.25) - (capital * payload["bonds_and_notes"] * 0.01) - capital_funds
        balances["realEstate"] = (capital * 0.25) - (capital * payload["realEstate"] * 0.01) - capital_funds
        balances["commodities"] = (capital * 0.25) - (capital * payload["commodities"] * 0.01) - capital_funds
    return {
        "risk": get_risk_for_portfolio(capital, portfolio_type, payload),
        "future_points": get_portfolio_value_x_year(
            get_risk_for_portfolio_helper(capital, portfolio_type, payload)
        ),
        "balancing": balances
    }

# print(
#     get_portfolio_value_x_year(
#         get_risk_for_portfolio_helper(100_000, "aggressive")
#     )
# )
