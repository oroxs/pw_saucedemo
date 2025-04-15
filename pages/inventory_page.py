from base.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_to_cart_button = "[data-test='add-to-cart-sauce-labs-backpack']"
        self.cart_icon = ".shopping_cart_link"

    def add_item_to_cart(self):
        self.click(self.add_to_cart_button)

    def go_to_cart(self):
        self.click(self.cart_icon)
