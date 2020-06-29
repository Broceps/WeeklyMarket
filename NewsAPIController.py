import requests

api_Key = "b9c6db2f275042799ddc7b06f3c75f11"
week_start_date = "2020-06-22"
week_end_date = "2020-06-26"
keyword = "NVDA"

req = requests.get("https://newsapi.org/v2/everything?q=" + keyword +"&from=" + week_start_date + "&to=" + week_end_date + "&sortBy=popularity&apiKey=" + api_Key)
result = req.json()

articles = result["articles"]
print("article found: ", articles[0]["title"])
print("link: ", articles[0]["url"])


