import requests

class NewsAPIController:
    _api_Key = open("../_files/news_api_key.txt").read()

    def fetch_news(self, start, end, company):
        start = start
        end = end
        company = company
        url = "https://newsapi.org/v2/everything?q=" + company + "&from=" + start + "&to=" + end + \
              "&sortBy=popularity&apiKey=" + self._api_Key

        req = requests.get(url)
        result = req.json()

        articles = result["articles"]
        article = articles[0]["title"]
        link = articles[0]["url"]
        res = {"article": article, "link": link}
        return res


