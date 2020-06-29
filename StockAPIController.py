import requests

stock_api_key = open('files/stock_api_key.txt').read()

key = "7FLIE5EAL5APIPVC"
stock = "GOOGL"
interval_daily = "DAILY"
interval_weekly = "WEEKLY"
date = "2020-06-26"
high = "2. high"
low = "3. low"
close = "4. close"
url = "https://www.alphavantage.co/query?function=TIME_SERIES_" + interval_weekly + "&symbol=" + stock + "&apikey=" + stock_api_key

r = requests.get(url)

companies = ["NVDA", "AAPL", "FB", "NFLX", "MFST", "GOOGL", "WMT", "JPM"]



'DAILY'
# daily_high = round(float((r.json()["Time Series (Daily)"][date][high])), 2)
# daily_low = round(float((r.json()["Time Series (Daily)"][date][low])), 2)
# daily_close = round(float((r.json()["Time Series (Daily)"][date][close])), 2)


'WEEKLY'
# weekly_high = round(float((r.json()["Weekly Time Series"][date][high])), 2)
weekly_low = round(float((r.json()["Weekly Time Series"][date][low])), 2)
# weekly_close = round(float((r.json()["Weekly Time Series"][date][close])), 2)


'Prints Statements'
# print(daily_high)
# print(daily_low)
# print(daily_close)

# print(weekly_high)
print(weekly_low)
# print(weekly_close)


# try:

# Exception:
    # pass


# print(r.json()['Meta Data'])