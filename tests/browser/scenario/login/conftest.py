from pytest_bdd import parsers, when, given, then

from lib.browser.pages.login_page import Login_page


@then('validate user logs with employee credentials and access Aspire portal homepage.')
def home_page(browser):
    login_pages = Login_page(browser)
    login_pages.verify_home_page()
