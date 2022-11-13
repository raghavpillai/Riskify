import json
import requests
from threading import Thread
import os
from sqlitedict import SqliteDict

db = SqliteDict("risk_analysis.sqlite")


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


def get_risk_for_portfolio(capital, portfolio_type):
    # if db.get(portfolio_type):
    #     print("CACHE ACCESSED FOR RISK_ANALYSIS")
    #     return db[portfolio_type]

    risks = get_risk_for_portfolio_helper(capital, portfolio_type)
    fields = {
        "alpha": 0.05,
        "portfolios": [{"portfolioValues": [int(risks[i]) for i in risks]}],
    }
    print(fields)
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

    db[portfolio_type] = {portfolio_type: risk}
    db.commit()

    return {portfolio_type: risk}
