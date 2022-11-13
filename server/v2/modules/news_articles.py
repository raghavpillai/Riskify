import yfinance as yf
import random

dic = {
    "VOO": ["Index Fund ETF", "Index Fund"],
    "VEA": ["Markets Index Fund ETF", "Market Fund"],
    "VWO": ["Stock Index Fund ETF", "Stock Index"],
    "IVOV": ["Mid-Cap 400 Value Index Fund ETF", "Mid-Cap 400 Index"],
    "VIOV": ["Small Cap 600 Value ETF", "Small-Cap 600 Index"],
    "VNQ": ["Real Estate Index Fund ETF", "Real Estate"],
    "VGLT": ["Long-Term Treasury Index Fund ETF", "Long-Term Treasury Index"],
    "VGIT": ["Intermediate-Term Treasury Index Fd ETF", "Mid-Term Treasury Index"],
    "VTI": ["Total Stock Market Index", "Total Market Index"],
    "SCHP": ["Treasury Inflation-Protected Securities", "Inflation-Protected Securities"],
    "VT": ["Vanguard Total World Stock", "Total World Stock"],
    "SGOL": ["Physical Gold Shares", "Physical Gold"],
    "VGSH": ["Vanguard Short-Term Treasury Index Fund", "Short-Term Index Fund"],
    "VTIP": ["Short-Term Inflation-Protected", "Short-Term Inflation-Protected"],
}

def get_news_articles(holdings_arr):
    amount_of_articles = int(10 / len(holdings_arr))
    articles = []

    for index, holding in enumerate(holdings_arr):
        if index == len(holdings_arr) - 1:
            amount_of_articles += (10 % amount_of_articles)
        for news in random.sample(yf.Ticker(dic[holding][0]).news, amount_of_articles):
            article = {}
            article["title"] = news["title"]
            article["link"] = news["link"]
            article["author"] = news["publisher"]
            article["topic"] = dic[holding][1]
            try:
                article["image"] = news["thumbnail"]["resolutions"][1]["url"]
            except:
                article["image"] = "https://s.yimg.com/uu/api/res/1.2/4JDV5cR1_5K7EMvoXVo7yg--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/simply_wall_st__316/f99e03d6864d27459bdfbebc0a8e18a3"
            articles.append(article)

    return articles[:10]


articles = get_news_articles(['VOO', 'IVOV', 'VNQ'])
print(articles)