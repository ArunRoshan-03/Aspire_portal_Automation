import time

import pytest as pytest
from selenium import webdriver
from pytest_bdd import given, then, when, parsers

from lib.browser.pages.login_page import Login_page
from lib.util.constants import website_url


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()


@given('Aspire application is launched')
def aspire_url(browser):
    browser.get(website_url)
    login_pages = Login_page(browser)
    login_pages.aspire_login_text()


@given(parsers.parse("login into aspire portal page as a {user_type:w}"))
def login_user(browser, user_type):
    login_pages = Login_page(browser)
    login_pages.user_login(user_type)


@then('validate user navigating to aspire portal home page')
def aspire_home_page(browser):
    login_pages = Login_page(browser)
    login_pages.verify_home_page_reload()
