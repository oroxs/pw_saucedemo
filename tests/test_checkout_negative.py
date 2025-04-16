from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def login_and_go_to_checkout(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(page)
    cart.click_checkout()

    return CheckoutPage(page)


def test_checkout_without_any_input(page):
    checkout = login_and_go_to_checkout(page)
    checkout.fill_info("", "", "")
    error = checkout.get_error_message()
    assert error == "Error: First Name is required"

def test_checkout_without_last_name(page):
    checkout = login_and_go_to_checkout(page)
    checkout.fill_info("Vardy", "", "40123")
    error = checkout.get_error_message()
    assert error == "Error: Last Name is required"

def test_checkout_without_postal_code(page):
    checkout = login_and_go_to_checkout(page)
    checkout.fill_info("Vardy", "QA", "")
    error = checkout.get_error_message()
    assert error == "Error: Postal Code is required"