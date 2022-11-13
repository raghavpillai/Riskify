import json
import requests
import os
from sqlitedict import SqliteDict

db = SqliteDict("risk_analysis.sqlite")

file_dir = os.path.dirname(os.path.realpath("__file__"))


def process_file(file_name):
    values = []
    file = open(file_name)
    data = json.load(file)
    for i in data:
        values.append(float(data[i]["Close"]))
    file.close()
    return values


def get_risk_for_portfolio_helper(capital, portfolio_type):
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
    else:  # ultra_conservative
        return {
            "VT": capital * 0.1,
            "VIOV": capital * 0.03,
            "VNQ": capital * 0.02,
            "SGOL": capital * 0.05,
            "VGIT": capital * 0.2,
            "VGSH": capital * 0.4,
            "VTIP": capital * 0.2,
        }


def future_portfolio_values(capital, portfolio_type):
    return get_portfolio_value_x_year(
        get_risk_for_portfolio_helper(capital, portfolio_type)
    )


def get_risk_for_portfolio(capital, portfolio_type):
    if db.get(f"{portfolio_type}_{capital}"):
        print("CACHE ACCESSED FOR RISK_ANALYSIS")
        return db[f"{portfolio_type}_{capital}"]

    risks = future_portfolio_values(capital, portfolio_type)
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


def get_portfolio_value_x_year(portfolio):
    file = open(os.path.join(file_dir, f"new_monte_carlo.json"))
    data = json.load(file)
    projected_portfolio_value = [0] * 26

    for ticker, value in portfolio.items():
        ticker = ticker.lower()

        # years 0-25 of the ticker
        for i in range(0, len(data[ticker])):
            # finding mean_price at that year
            mean_price = float(data[ticker][f"{i}"]["mean_price"])
            # ratio change of this ticker, (future / now)
            ratio_change = mean_price / float(
                data[ticker][f"{i - 1 if i > 0 else i}"]["mean_price"]
            )
            # add this tickers new value to that year of the projected portfolio
            projected_portfolio_value[i] += value * ratio_change

    file.close()
    return projected_portfolio_value


# print(
#     get_portfolio_value_x_year(
#         get_risk_for_portfolio_helper(100_000, "aggressive")
#     )
# )
