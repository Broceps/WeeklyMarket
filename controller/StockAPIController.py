import requests

# print(r.json()['Meta Data'])

# companies = ["NVDA", "AAPL", "FB", "NFLX", "MFST", "GOOGL", "WMT", "JPM"]

class StockAPIController:
    _stock_api_key = open('../_files/stock_api_key.txt').read()

    def daily_prices(self, date, stock):
        date = date
        stock = stock
        interval_daily = "DAILY"
        high = "2. high"
        low = "3. low"
        close = "4. close"
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_" + interval_daily + "&symbol="\
              + stock + "&apikey=" + self._stock_api_key
        r = requests.get(url)

        high_price = round(float((r.json()["Time Series (Daily)"][date][high])), 2)
        low_price = round(float((r.json()["Time Series (Daily)"][date][low])), 2)
        close_price = round(float((r.json()["Time Series (Daily)"][date][close])), 2)

        result = {"Company": stock, "Highest Price ": high_price, "Lowest Price: ": low_price,
                  "Close Price: ": close_price}
        return result


    def weekly_prices(self, date, stock):
        date = date
        stock = stock
        interval_weekly = "WEEKLY"
        high = "2. high"
        low = "3. low"
        close = "4. close"
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_" + interval_weekly + "&symbol=" + stock\
              + "&apikey=" + self._stock_api_key
        r = requests.get(url)

        high_price = round(float((r.json()["Weekly Time Series"][date][high])), 2)
        low_price = round(float((r.json()["Weekly Time Series"][date][low])), 2)
        close_price = round(float((r.json()["Weekly Time Series"][date][close])), 2)

        result = {"Company": stock, "Highest Price ": high_price, "Lowest Price: ": low_price,
                  "Close Price: ": close_price}
        return result

