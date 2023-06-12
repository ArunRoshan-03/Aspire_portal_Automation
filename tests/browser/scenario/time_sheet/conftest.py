from pytest_bdd import then, when

from lib.browser.pages.timesheet_page import TimeSheet_Page


@then('I validate the time sheet link')
def validate_time_sheet_link(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_time_sheet_link()


@when('I click on the time sheet link on the homepage')
def click_time_sheet_link(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.click_time_sheet_link()


@then('I validate the time sheet page')
def validate_time_sheet_page(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_time_sheet_page()


@then("I validate the current week's dates")
def validate_current_weeks_date(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_current_dates()


@when('I enter the timings from the entire week to the time sheet')
def enter_timing_to_time_sheet(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.click_activity_dropdown_box()
    timesheet_page.entire_week_timing()


@then('I validate activities and save time sheet.')
def validate_activities_and_save_time_sheet(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.click_save_button()
    timesheet_page.verify_activity_timing()
