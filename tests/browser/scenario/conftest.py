import pytest as pytest
from selenium import webdriver
from pytest_bdd import given, then, when

from lib.browser.pages.login_page import Login_page
from lib.util.constants import website_url


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()


@given('user launch browser and user enter Aspire url')
def aspire_url(browser):
    browser.get(website_url)


@given('I navigated to the Aspire login_page is displayed')
def aspire_login_page(browser):
    login_pages = Login_page(browser)
    login_pages.aspire_login_text()


@when("I fill the username <email_id> and password <password> on login_page")
def login_details(browser, email_id, password):
    login_pages = Login_page(browser)
    login_pages.user_email_id_credentials(email_id)
    login_pages.user_password_credentials(password)


@when("I click login button on the login button")
def login_button(browser):
    login_pages = Login_page(browser)
    # login_pages.click_captcha_button()
    login_pages.click_login_button()
