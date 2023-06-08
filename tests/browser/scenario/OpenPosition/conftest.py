from pytest_bdd import then

from lib.browser.pages.openposition_page import OpenPosition_Page


@then('I validate the open position page')
def open_position_page(browser):
    openPosition_page = OpenPosition_Page(browser)
    openPosition_page.click_open_position()


@then('I validate the list of job openings in the job openings table')
def validate_job_open_position(browser):
    openPosition_page = OpenPosition_Page(browser)
    openPosition_page.click_open_position()
    openPosition_page.verify_job_position()
