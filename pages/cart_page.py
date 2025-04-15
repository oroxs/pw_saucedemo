from base.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = "[data-test='checkout']"

    def click_checkout(self):
        self.click(self.checkout_button)
