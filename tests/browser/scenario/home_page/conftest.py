from pytest_bdd import parsers, when, given, then

from lib.browser.pages.home_page import *


@then('validate the list of links that appears on the home page sidebar.')
def validate_home_page_sidebar(browser):
    home_page = Home_page(browser)
    home_page.verify_side_bar_link()


@then('verify that the user is navigating the particular page.')
def verify_navigating_particular_page(browser):
    home_page = Home_page(browser)
    home_page.verify_side_bar_page()
