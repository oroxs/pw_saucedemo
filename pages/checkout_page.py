from base.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name = "[data-test='firstName']"
        self.last_name = "[data-test='lastName']"
        self.postal_code = "[data-test='postalCode']"
        self.continue_button = "[data-test='continue']"
        self.finish_button = "[data-test='finish']"
        self.error_msg = "[data-test='error']"

    def fill_info(self, first, last, zip_code):
        if first:
            self.fill(self.first_name, first)
        if last:
            self.fill(self.last_name, last)
        if zip_code:
            self.fill(self.postal_code, zip_code)
        self.click(self.continue_button)

    def finish_checkout(self):
        self.click(self.finish_button)
    
    def get_error_message(self):
        if self.is_visible(self.error_msg):
            return self.get_text(self.error_msg)
        return None
