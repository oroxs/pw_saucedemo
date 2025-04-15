from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_checkout_flow(page):
    # Login
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Add to cart
    inventory = InventoryPage(page)
    inventory.add_item_to_cart()
    inventory.go_to_cart()

    # Checkout
    cart = CartPage(page)
    cart.click_checkout()

    checkout = CheckoutPage(page)
    checkout.fill_info("Vardy", "QA", "40123")
    checkout.finish_checkout()

    # Verify complete
    complete = CheckoutCompletePage(page)
    assert complete.is_order_complete()
