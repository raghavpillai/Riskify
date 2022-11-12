import yfinance as yf

tick = yf.Ticker("VTIP")

# get historical market data
hist = tick.history(period="max")
hist.to_csv(f"{tick.ticker.lower()}_historical_data.csv")
