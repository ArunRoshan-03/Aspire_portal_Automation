from pytest_bdd import then, when, given

from lib.browser.pages.login_page import Login_page
from lib.browser.pages.openposition_page import OpenPosition_Page


@then('I validate the open position link')
def validate_open_position_link(browser):
    openPosition_page = OpenPosition_Page(browser)
    openPosition_page.verify_open_position_link()


@when('I click on the open position link')
def click_open_position_link(browser):
    openPosition_page = OpenPosition_Page(browser)
    openPosition_page.click_open_position_link()


@when('I navigated to job openings page')
def open_position_page(browser):
    openPosition_page = OpenPosition_Page(browser)
    openPosition_page.open_position_page()


@then('I validate the job openings page')
def validate_open_position_page(browser):
    openPosition_page = OpenPosition_Page(browser)
    openPosition_page.verify_open_position_page()


@then('I validate the list of job openings')
def validate_job_open_position(browser):
    openPosition_page = OpenPosition_Page(browser)
    openPosition_page.verify_job_positions()

