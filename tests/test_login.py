from pages.login_page import LoginPage

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_logged_in(), "Login failed, inventory page not visible."

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("invalid_user", "wrong_password")
    error = login_page.get_error_message()
    assert error is not None
    assert "Username and password do not match" in error or "do not match" in error
