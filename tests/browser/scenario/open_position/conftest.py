from pytest_bdd import then, when, given

from lib.browser.pages.login_page import Login_page
from lib.browser.pages.openposition_page import OpenPosition_Page


@then('verify the open position link is displayed on homepage.')
def validate_open_position_link(browser):
    openPosition_page = OpenPosition_Page(browser)
    openPosition_page.verify_open_position_link()


@when('click on the open position link on the homepage')
def click_open_position_link(browser):
    openPosition_page = OpenPosition_Page(browser)
    openPosition_page.click_open_position_link()


@then('validate user navigating to open position page')
def validate_navigating_position_page(browser):
    openPosition_page = OpenPosition_Page(browser)
    openPosition_page.verify_open_position_page_reload()


@then('verify the open position page title that appears on the open sheet page.')
def validate_open_position_page(browser):
    openPosition_page = OpenPosition_Page(browser)
    openPosition_page.verify_open_position_page()


@then('validate the job title list that appears on the open position page.')
def validate_job_open_position(browser):
    openPosition_page = OpenPosition_Page(browser)
    openPosition_page.verify_job_positions()


@when('navigating to open position page')
def navigating_timesheet_page(browser):
    openPosition_page = OpenPosition_Page(browser)
    openPosition_page.open_position_page_reload()
