from controller import NewsAPIController, StockAPIController


class MainDriver:
    news_controller = NewsAPIController.NewsAPIController()
    stock_controller = StockAPIController.StockAPIController()

    _newsletter_msg = "Dear {0}, here is your weekly newsletter!\n" \
                      "--------\n{1}\n--------\n" \
                      "lowest price: ${2}, highest price: ${3}, closing price: {4}\n" \
                      "{1} was mentioned in the following articles this week:\n" \
                      "{5}\n" \
                      "link: {6}"

    def print_newsletter(self, name, company):
        stock_data = self.stock_controller.weekly_prices("2020-06-26",company)
        article_data = self.news_controller.fetch_news("2020-06-22", "2020-06-26",company)

        print(self._newsletter_msg.format(
            name, company, stock_data.get("Lowest Price"),stock_data.get("Highest Price"),
            stock_data.get("Close Price"), article_data.get("article"),article_data.get("link") ))


d = MainDriver()
d.print_newsletter("Martin", "NVDA")