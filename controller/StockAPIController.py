import requests

stock_api_key = open('_files/stock_api_key.txt').read()

# companies = ["NVDA", "AAPL", "FB", "NFLX", "MFST", "GOOGL", "WMT", "JPM"]

class StockAPIController():


    def daily_prices(self):
        date = "2020-06-26"
        stock = "FB"
        interval_daily = "DAILY"
        high = "2. high"
        low = "3. low"
        close = "4. close"
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_" + interval_daily + "&symbol=" + stock + "&apikey=" + stock_api_key
        r = requests.get(url)

        high_price = round(float((r.json()["Time Series (Daily)"][date][high])), 2)
        low_price = round(float((r.json()["Time Series (Daily)"][date][low])), 2)
        close_price = round(float((r.json()["Time Series (Daily)"][date][close])), 2)

        result = {"Company": stock, "Highest Price ": high_price, "Lowest Price: ": low_price, "Close Price: ": close_price}
        return result
        # print(round(float((r.json()["Time Series (Daily)"][date][high])), 2))
        # print(round(float((r.json()["Time Series (Daily)"][date][low])), 2))
        # print(round(float((r.json()["Time Series (Daily)"][date][close])), 2))


    # def weekly_prices(self):
    #     date = "2020-06-26"
    #     stock = "FB"
    #     interval_weekly = "WEEKLY"
    #     high = "2. high"
    #     low = "3. low"
    #     close = "4. close"
    #     url = "https://www.alphavantage.co/query?function=TIME_SERIES_" + interval_weekly + "&symbol=" + stock + "&apikey=" + stock_api_key
    #     r = requests.get(url)
    #
    #     # high_price =
    #     # low_price =
    #     # close_price =
    #
    #     print(round(float((r.json()["Weekly Time Series"][date][high])), 2))
    #     print(round(float((r.json()["Weekly Time Series"][date][low])), 2))
    #     print(round(float((r.json()["Weekly Time Series"][date][close])), 2))
    # weekly_prices()

# StockAPIController()









'DAILY'
# daily_high = round(float((r.json()["Time Series (Daily)"][date][high])), 2)
# daily_low = round(float((r.json()["Time Series (Daily)"][date][low])), 2)
# daily_close = round(float((r.json()["Time Series (Daily)"][date][close])), 2)


'WEEKLY'
# weekly_high = round(float((r.json()["Weekly Time Series"][date][high])), 2)
# weekly_low = round(float((r.json()["Weekly Time Series"][date][low])), 2)
# weekly_close = round(float((r.json()["Weekly Time Series"][date][close])), 2)


'Prints Statements'
# print(daily_high)
# print(daily_low)
# print(daily_close)

# print(weekly_high)
# print(weekly_low)
# print(weekly_close)


# try:

# Exception:
    # pass

# print(r.json()['Meta Data'])