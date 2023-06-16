from datetime import time

from pytest_bdd import then, when, given, parsers

from lib.browser.pages.login_page import Login_page
from lib.browser.pages.timesheet_page import TimeSheet_Page


@then('verify the time sheet link is displayed on homepage.')
def validate_time_sheet_link(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_time_sheet_link()


@when('I click on the time sheet link on the homepage')
def click_time_sheet_link(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.click_time_sheet_link()


@then('validate user navigating to timesheet page')
def validate_navigating_timesheet_page(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_timesheet_page_reload()


@when('timesheet page is loaded')
def loaded_timesheet_page(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.timesheet_page_reload()


@then('verify the time sheet page title that appears on the time sheet page.')
def validate_time_sheet_page(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_time_sheet_page()


@given(parsers.parse("login into aspire portal page as a {user_type:w}"))
def login_user(browser, user_type):
    login_pages = Login_page(browser)
    login_pages.user_login(user_type)


@then("validate the current week's dates that appear on the time sheet page.")
def validate_current_weeks_date(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_current_dates()


@when('I enter the working hours for the week and save the timesheet')
def enter_timing_and_save_time_sheet(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.click_activity_dropdown_box()
    timesheet_page.entire_week_timing()
    timesheet_page.click_save_button()


@then('validate activities saved on the time sheet.')
def validate_activities_saved_on_time_sheet(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_activity_timing()


@when('I enter the working hours for the week and submit the timesheet')
def enter_timing_and_submit_time_sheet(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.click_activity_dropdown_box()
    timesheet_page.entire_week_timing()
    timesheet_page.click_submit_button()


@then('validate activities submitted on time sheet.')
def validate_activities_submit_on_time_sheet(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_submitted_label_text()


@when('I log out and return to the login page')
def logout_and_loads_login_page(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.click_logout_button()


@when(parsers.parse("I login into aspire portal page as a {user_type:w}."))
def login_user(browser, user_type):
    login_pages = Login_page(browser)
    login_pages.user_login(user_type)


@when('I click the reports button on the time sheet page.')
def click_reports_button(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.click_reports_button()


@when('the reports page is loaded.')
def loaded_reports_page(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.reload_reports_page()


@when('I select the client, start date and end start data on the project wise table.')
def select_client_start_data_and_end_date(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.click_client_dropdown_box()
    timesheet_page.select_start_date()
    timesheet_page.select_end_date()


@when('I click the export button')
def click_export_button(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.click_export_button()


@then('the exported data as appear on the project wise table.')
def export_data_loaded(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.export_data_tabel_is_displayed()


@then('I validate the weekday timing of the employee.')
def validate_weekday_timing(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.working_timing_table()


@then('If the employee has less than working hours,an email should be sent to the employee.')
def verify_email_send_to_employees(browser):
    timesheet_page = TimeSheet_Page(browser)
    timesheet_page.verify_sending_email_to_employee()
