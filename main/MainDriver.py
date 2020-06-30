from controller import NewsAPIController, StockAPIController
import controller


class MainDriver:
    _news_controller = NewsAPIController()
    _stock_controller = StockAPIController()

    _newsletter_msg = "Dear {0}, here is your weekly newsletter!\n" \
                      "--------\n{1}--------\n" \
                      "lowest price: ${2}, highest price: ${3}, closing price: {4}\n" \
                      "{1} was mentioned in the following articles this week:\n" \
                      "{5}"

    def print_newsletter(self, name, company):
        stock_data = self.S_stock_controller.
        new = self._news_controller.

        print()
