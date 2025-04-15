from base.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_msg = "[data-test='error']"
        self.inventory_title = ".title"

    def load(self):
        self.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def get_error_message(self):
        if self.is_visible(self.error_msg):
            return self.get_text(self.error_msg)
        return None

    def is_logged_in(self):
        return self.is_visible(self.inventory_title)
