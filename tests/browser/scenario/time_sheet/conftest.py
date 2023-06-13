from pytest_bdd import then, when

from lib.browser.pages.timesheet_page import TimeSheet_Page


@then('verify the time sheet link is displayed on homepage.')
def validate_time_sheet_link(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_time_sheet_link()


@when('click on the time sheet link on the homepage')
def click_time_sheet_link(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.click_time_sheet_link()


@then('validate user navigating to timesheet page')
def validate_navigating_timesheet_page(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_timesheet_page_reload()


@when('navigating to timesheet page')
def navigating_timesheet_page(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.timesheet_page_reload()


@then('verify the time sheet page title that appears on the time sheet page.')
def validate_time_sheet_page(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_time_sheet_page()


@then("validate the current week's dates that appear on the time sheet page.")
def validate_current_weeks_date(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_current_dates()


@when('enter the times for the entire week and then save the time sheet.')
def enter_timing_and_save_time_sheet(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.click_activity_dropdown_box()
    timesheet_page.entire_week_timing()
    timesheet_page.click_save_button()


@then('validate activities saved on the time sheet.')
def validate_activities_saved_on_time_sheet(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_activity_timing()


@when('enter the times for the entire week and then submit the time sheet.')
def enter_timing_and_submit_time_sheet(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.click_activity_dropdown_box()
    timesheet_page.entire_week_timing()
    timesheet_page.click_submit_button()


@then('validate activities submitted on time sheet.')
def validate_activities_submit_on_time_sheet(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_submitted_label_text()
