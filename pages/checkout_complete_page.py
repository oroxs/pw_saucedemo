from base.base_page import BasePage

class CheckoutCompletePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.complete_text = ".complete-header"

    def is_order_complete(self):
        return self.get_text(self.complete_text) == "Thank you for your order!"
