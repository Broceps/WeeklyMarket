from controller import NewsAPIController, StockAPIController, DBController, EmailController


class MainDriver:
    news_controller = NewsAPIController.NewsAPIController()
    stock_controller = StockAPIController.StockAPIController()
    db_controller = DBController.DBController()
    email_controller = EmailController.EmailController()

    _newsletter_msg = "Dear {0}, here is your weekly newsletter!\n" \
                      "--------\n{1}\n--------\n" \
                      "Lowest price: ${2} \n" \
                      "Highest price: ${3} \n" \
                      "Closing price: {4}\n" \
                      "{1} was mentioned in the following articles this week:\n" \
                      "{5}\n" \
                      "link: {6}"

    def print_newsletter(self, name, company):
        stock_data = self.stock_controller.weekly_prices("2020-06-26", company)
        article_data = self.news_controller.fetch_news("2020-06-22", "2020-06-26", company)

        print(self._newsletter_msg.format(
            name, company, stock_data.get("Lowest Price"), stock_data.get("Highest Price"),
            stock_data.get("Close Price"), article_data.get("article"), article_data.get("link")))

    def send_newsletter_email_to_all_users(self):
        user_list = self.db_controller.get_emails_and_ticker()
        for row in user_list:
            email = row[0]
            ticker = row[1]
            name = row[2]
            stock_data = self.stock_controller.weekly_prices("2020-06-26", ticker)
            article_data = self.news_controller.fetch_news("2020-06-22", "2020-06-26", ticker)
            msg = self._newsletter_msg.format(
            name, ticker, stock_data.get("Lowest Price"), stock_data.get("Highest Price"),
            stock_data.get("Close Price"), article_data.get("article"), article_data.get("link"))
            self.email_controller.email_sendout(ticker,msg,email)


d = MainDriver()
d.send_newsletter_email_to_all_users()