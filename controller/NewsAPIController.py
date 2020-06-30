import requests

class NewsAPIController:
    _api_Key = open("../_files/news_api_key.txt").read()

    def fetch_news(self, start, end, company):
        start = start
        end = end
        company = company
        url = "https://newsapi.org/v2/everything?q=" + company +"&from=" + start + "&to=" + end + "&sortBy=popularity&apiKey=" + self._api_Key

        req = requests.get(url)
        result = req.json()

        articles = result["articles"]
        article = articles[0]["title"]
        link = articles[0]["url"]
        res =  {"article":article, "link":link}
        return res






#for testing purposes
week_start_date = "2020-06-22"
week_end_date = "2020-06-26"
keyword = "NVDA"

c = NewsAPIController()
c.fetch_news(week_start_date, week_end_date ,keyword)
