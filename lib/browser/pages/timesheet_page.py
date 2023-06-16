import re
import time
from builtins import staticmethod

from selenium.webdriver.common.by import By

from lib.browser.pages.driver_commands import BasicActions
from lib.data.mail_data import *
from lib.data.timesheet_data import *
from lib.util.constants import *
from lib.util.email_generated import send_email
from lib.util.excelhandling import *
from lib.util.utilities import utilities


class TimeSheet_Page(BasicActions):

    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.button_index = None
        self.value = []

    # locator
    time_sheet_link_loc = (By.XPATH, "//span[normalize-space()='Timesheet']")
    time_sheet_page_loc = (By.XPATH, "//h1[@class='pull-left']")
    activity_dates_loc = (By.XPATH, "//*[@id='table_0']/tbody[1]/tr/th")
    weeks_dates_loc = (By.XPATH, "//*[@id='employeeTimesheet']/div[2]/table/tbody/tr/td[2]/b")
    monday_timing_text_box_loc = (By.XPATH, "(//input[@placeholder='H:m'])[1]")
    tuesday_timing_text_box_loc = (By.XPATH, "(//input[@placeholder='H:m'])[2]")
    wednesday_timing_text_box_loc = (By.XPATH, "(//input[@placeholder='H:m'])[3]")
    thursday_timing_text_box_loc = (By.XPATH, "(//input[@placeholder='H:m'])[4]")
    friday_timing_text_box_loc = (By.XPATH, "(//input[@placeholder='H:m'])[5]")
    saturday_timing_text_box_loc = (By.XPATH, "(//input[@placeholder='H:m'])[6]")
    sunday_timing_text_box_loc = (By.XPATH, "(//input[@placeholder='H:m'])[7]")
    okay_button_loc = (By.XPATH, "//*[@class='modal-content']/div/button[@class='btn btn-primary']")
    cancel_button_loc = (By.XPATH, "//*[@class='modal-content']/div/button[@class='close']")
    activity_drop_down_box_loc = (By.XPATH, "//b[@role='presentation']")
    activity_option_loc = (By.XPATH, "//ul[@class='select2-results__options']/li")
    save_button_loc = (By.XPATH, "//a[@id='e_0']")
    monday_data_text_box_loc = (By.XPATH, "//td[contains(@data-day,'Mon')]")
    tuesday_data_text_box_loc = (By.XPATH, "//td[contains(@data-day,'Tue')]")
    wednesday_data_text_box_loc = (By.XPATH, "//td[contains(@data-day,'Wed')]")
    thursday_data_text_box_loc = (By.XPATH, "//td[contains(@data-day,'Thu')]")
    friday_data_text_box_loc = (By.XPATH, "//td[contains(@data-day,'Fri')]")
    saturday_data_text_box_loc = (By.XPATH, "//td[contains(@data-day,'Sat')]")
    sunday_data_text_box_loc = (By.XPATH, "//td[contains(@data-day,'Sun')]")
    submit_for_approval_button_loc = (By.XPATH, "//a[@id='le_0']")
    submitted_label_text_loc = (By.XPATH, "//span[contains(@class,'Submitted')]")
    profile_image_label_loc = (
        By.XPATH, "//a[@class='nav-link dropdown-toggle text-muted waves-effect waves-dark pro-pic']")
    logout_button_loc = (By.XPATH, "//button[normalize-space()='Logout']")
    reports_button_loc = (By.XPATH, "//a[normalize-space()='Reports']")
    client_drop_down_box_loc = (By.XPATH, "(//b[@role='presentation'])[1]")
    client_option_loc = (By.XPATH, "//ul[@id='select2-selectClient-results']/li")
    start_date_loc = (By.XPATH, "//input[@id='startDate']")
    end_date_loc = (By.XPATH, "//input[@id='endDate']")
    export_button_loc = (By.XPATH, "//button[normalize-space()='Export']")
    export_data_table_loc = (By.XPATH, "//ul[@id='exportTab']//a[@id='exporthome-tab']")
    emp_Id_loc = (By.XPATH, "(//*[@id='exportTable']/thead/tr/th[1])[1]| //div[3]//div[1]/table/tbody/tr/td[1]")
    emp_monday_timing_data_loc = (
        By.XPATH, "(//*[@id='exportTable']/thead/tr/th[10])[1]| //div[3]//div[1]/table/tbody/tr/td[10] ")
    emp_tuesday_timing_data_loc = (
        By.XPATH, "(//*[@id='exportTable']/thead/tr/th[11])[1]| //div[3]//div[1]/table/tbody/tr/td[11] ")
    emp_wednesday_timing_data_loc = (
        By.XPATH, "(//*[@id='exportTable']/thead/tr/th[12])[1]| //div[3]//div[1]/table/tbody/tr/td[12] ")
    emp_thursday_timing_data_loc = (
        By.XPATH, "(//*[@id='exportTable']/thead/tr/th[13])[1]| //div[3]//div[1]/table/tbody/tr/td[13] ")
    emp_friday_timing_data_loc = (
        By.XPATH, "(//*[@id='exportTable']/thead/tr/th[14])[1]| //div[3]//div[1]/table/tbody/tr/td[14] ")

    # export_button_loc = (By.XPATH, "//button[normalize-space()='Export']")

    @property
    def time_sheet_link(self):
        return self.web_driver.find_element(*self.time_sheet_link_loc)

    @property
    def time_sheet_page(self):
        return self.web_driver.find_element(*self.time_sheet_page_loc)

    @property
    def week_dates_text(self):
        return self.web_driver.find_element(*self.weeks_dates_loc)

    @property
    def activity_dates(self):
        return self.web_driver.find_elements(*self.activity_dates_loc)

    @property
    def monday_timing_text_box(self):
        return self.web_driver.find_element(*self.monday_timing_text_box_loc)

    @property
    def tuesday_timing_text_box(self):
        return self.web_driver.find_element(*self.tuesday_timing_text_box_loc)

    @property
    def wednesday_timing_text_box(self):
        return self.web_driver.find_element(*self.wednesday_timing_text_box_loc)

    @property
    def thursday_timing_text_box(self):
        return self.web_driver.find_element(*self.thursday_timing_text_box_loc)

    @property
    def friday_timing_text_box(self):
        return self.web_driver.find_element(*self.friday_timing_text_box_loc)

    @property
    def saturday_timing_text_box(self):
        return self.web_driver.find_element(*self.saturday_timing_text_box_loc)

    @property
    def sunday_timing_text_box(self):
        return self.web_driver.find_element(*self.sunday_timing_text_box_loc)

    @property
    def okay_button(self):
        return self.web_driver.find_element(*self.okay_button_loc)

    @property
    def cancel_button(self):
        return self.web_driver.find_element(*self.cancel_button_loc)

    @property
    def activity_drop_down_box(self):
        return self.web_driver.find_element(*self.activity_drop_down_box_loc)

    @property
    def activity_option(self):
        return self.web_driver.find_element(*self.activity_option_loc)

    @property
    def save_button(self):
        return self.web_driver.find_element(*self.save_button_loc)

    @property
    def monday_data_text_box(self):
        return self.web_driver.find_element(*self.monday_data_text_box_loc)

    @property
    def tuesday_data_text_box(self):
        return self.web_driver.find_element(*self.tuesday_data_text_box_loc)

    @property
    def wednesday_data_text_box(self):
        return self.web_driver.find_element(*self.wednesday_data_text_box_loc)

    @property
    def thursday_data_text_box(self):
        return self.web_driver.find_element(*self.thursday_data_text_box_loc)

    @property
    def friday_data_text_box(self):
        return self.web_driver.find_element(*self.friday_data_text_box_loc)

    @property
    def saturday_data_text_box(self):
        return self.web_driver.find_element(*self.saturday_data_text_box_loc)

    @property
    def sunday_data_text_box(self):
        return self.web_driver.find_element(*self.sunday_data_text_box_loc)

    @property
    def submit_for_approval_button(self):
        return self.web_driver.find_element(*self.submit_for_approval_button_loc)

    @property
    def submitted_label_text(self):
        return self.web_driver.find_element(*self.submitted_label_text_loc)

    @property
    def profile_image_label(self):
        return self.web_driver.find_element(*self.profile_image_label_loc)

    @property
    def logout_button(self):
        return self.web_driver.find_element(*self.logout_button_loc)

    @property
    def reports_button(self):
        return self.web_driver.find_element(*self.reports_button_loc)

    @property
    def client_drop_down_box(self):
        return self.web_driver.find_element(*self.client_drop_down_box_loc)

    @property
    def client_option(self):
        return self.web_driver.find_element(*self.client_option_loc)

    @property
    def start_date_text_box(self):
        return self.web_driver.find_element(*self.start_date_loc)

    @property
    def end_date_text_box(self):
        return self.web_driver.find_element(*self.end_date_loc)

    @property
    def export_button(self):
        return self.web_driver.find_element(*self.export_button_loc)

    @property
    def export_data_table(self):
        return self.web_driver.find_element(*self.export_data_table_loc)

    @property
    def emp_Id_data(self):
        return self.web_driver.find_elements(*self.emp_Id_loc)

    @property
    def emp_monday_timing_data(self):
        return self.web_driver.find_elements(*self.emp_monday_timing_data_loc)

    @property
    def emp_tuesday_timing_data(self):
        return self.web_driver.find_elements(*self.emp_tuesday_timing_data_loc)

    @property
    def emp_wednesday_timing_data(self):
        return self.web_driver.find_elements(*self.emp_wednesday_timing_data_loc)

    @property
    def emp_thursday_timing_data(self):
        return self.web_driver.find_elements(*self.emp_thursday_timing_data_loc)

    @property
    def emp_friday_timing_data(self):
        return self.web_driver.find_elements(*self.emp_friday_timing_data_loc)

    def verify_time_sheet_link(self):
        self.element_is_displayed(self.time_sheet_link)
        self.assert_element_value(self.time_sheet_link, time_sheet_link_text)

    def click_time_sheet_link(self):
        self.wait_for_elements_present(self.time_sheet_link_loc)
        self.click_element(self.time_sheet_link)

    def verify_time_sheet_page(self):
        self.wait_for_elements_present(self.time_sheet_page_loc)
        self.assert_element_value(self.time_sheet_page, time_sheet_page)

    def verify_current_dates(self):
        self.wait_for_elements_present(self.activity_dates_loc)
        current_date = []
        for dates in range(1, len(self.activity_dates), 6):
            weeks_date = self.get_text_element(self.activity_dates[dates])
            current_date.append(weeks_date)

        trimmed_dates = [re.sub(r'[^0-9/]', '', date.strip('\n')) for date in current_date]
        expected_dates = ' - '.join(trimmed_dates)
        actual_dates = self.get_text_element(self.week_dates_text)
        utilities.verify_string_text(expected_dates, actual_dates)

    def enter_monday_timings(self, timings_data):
        self.wait_for_elements_present(self.monday_timing_text_box_loc)
        self.clear_by_xpath(self.monday_timing_text_box)
        self.enter_text_field(self.monday_timing_text_box, timings_data)

    def enter_tuesday_timings(self, timings_data):
        self.wait_for_elements_present(self.tuesday_timing_text_box_loc)
        self.clear_by_xpath(self.tuesday_timing_text_box)
        self.enter_text_field(self.tuesday_timing_text_box, timings_data)

    def enter_wednesday_timings(self, timings_data):
        self.wait_for_elements_present(self.wednesday_timing_text_box_loc)
        self.clear_by_xpath(self.wednesday_timing_text_box)
        self.enter_text_field(self.wednesday_timing_text_box, timings_data)

    def enter_thursday_timings(self, timings_data):
        self.wait_for_elements_present(self.thursday_timing_text_box_loc)
        self.clear_by_xpath(self.thursday_timing_text_box)
        self.enter_text_field(self.thursday_timing_text_box, timings_data)

    def enter_friday_timings(self, timings_data):
        self.wait_for_elements_present(self.friday_timing_text_box_loc)
        self.clear_by_xpath(self.friday_timing_text_box)
        self.enter_text_field(self.friday_timing_text_box, timings_data)

    def enter_saturday_timings(self, timings_data):
        self.clear_by_xpath(self.saturday_timing_text_box)
        self.wait_for_elements_present(self.saturday_timing_text_box_loc)
        self.enter_text_field(self.saturday_timing_text_box, timings_data)

    def enter_sunday_timings(self, timings_data):
        self.wait_for_elements_present(self.sunday_timing_text_box_loc)
        self.clear_by_xpath(self.sunday_timing_text_box)
        self.enter_text_field(self.sunday_timing_text_box, timings_data)

    def entire_week_timing(self):
        self.enter_monday_timings(common_timing)
        self.enter_tuesday_timings(common_timing)
        self.enter_wednesday_timings(common_timing)
        self.enter_thursday_timings(common_timing)
        self.enter_friday_timings(common_timing)

    def click_activity_dropdown_box(self):
        self.click_element(self.activity_drop_down_box)
        self.select_by_xpath(self.activity_option, documentation_reports_activity)

    def click_save_button(self):
        self.wait_for_elements_present(self.save_button_loc)
        self.click_element(self.save_button)

    def verify_monday_timing_text(self):
        self.wait_for_elements_present(self.monday_timing_text_box_loc)
        actual_monday_timing_text = self.get_text_element(self.monday_data_text_box)
        self.assert_element_value(self.monday_data_text_box, actual_monday_timing_text)

    def verify_tuesday_timing_text(self):
        self.wait_for_elements_present(self.tuesday_timing_text_box_loc)
        actual_tuesday_timing_text = self.get_text_element(self.tuesday_data_text_box)
        self.assert_element_value(self.tuesday_data_text_box, actual_tuesday_timing_text)

    def verify_wednesday_timing_text(self):
        self.wait_for_elements_present(self.wednesday_timing_text_box_loc)
        actual_wednesday_timing_text = self.get_text_element(self.wednesday_data_text_box)
        self.assert_element_value(self.wednesday_data_text_box, actual_wednesday_timing_text)

    def verify_thursday_timing_text(self):
        self.wait_for_elements_present(self.thursday_timing_text_box_loc)
        actual_monday_timing_text = self.get_text_element(self.thursday_data_text_box)
        self.assert_element_value(self.monday_data_text_box, actual_monday_timing_text)

    def verify_friday_timing_text(self):
        self.wait_for_elements_present(self.friday_timing_text_box_loc)
        actual_friday_timing_text = self.get_text_element(self.friday_data_text_box)
        self.assert_element_value(self.friday_data_text_box, actual_friday_timing_text)

    def verify_saturday_timing_text(self):
        self.wait_for_elements_present(self.saturday_timing_text_box_loc)
        actual_saturday_timing_text = self.get_text_element(self.saturday_data_text_box)
        self.assert_element_value(self.saturday_data_text_box, actual_saturday_timing_text)

    def verify_sunday_timing_text(self):
        self.wait_for_elements_present(self.sunday_timing_text_box_loc)
        actual_sunday_timing_text = self.get_text_element(self.sunday_data_text_box)
        self.assert_element_value(self.sunday_data_text_box, actual_sunday_timing_text)

    def verify_activity_timing(self):
        self.verify_monday_timing_text()
        self.verify_tuesday_timing_text()
        self.verify_wednesday_timing_text()
        self.verify_thursday_timing_text()
        self.verify_saturday_timing_text()
        self.verify_sunday_timing_text()

    def click_submit_button(self):
        self.click_element(self.submit_for_approval_button)

    def timesheet_page_reload(self):
        self.page_reload()

    def verify_timesheet_page_reload(self):
        self.check_page_reload(time_sheet_url)

    def verify_submitted_label_text(self):
        self.wait_for_elements_present(self.submitted_label_text_loc)
        self.page_reload()
        self.assert_element_value(self.submitted_label_text, submitted_text)

    def click_logout_button(self):
        self.wait_for_elements_present(self.profile_image_label_loc)
        self.click_element(self.profile_image_label)
        self.wait_for_elements_present(self.logout_button_loc)
        self.click_element(self.logout_button)
        self.page_reload()

    def click_reports_button(self):
        self.wait_for_elements_present(self.reports_button_loc)
        self.click_element(self.reports_button)

    def reload_reports_page(self):
        self.page_reload()

    def click_client_dropdown_box(self):
        self.click_element(self.client_drop_down_box)
        self.select_by_xpath(self.client_option, client_name)

    def select_start_date(self):
        self.wait_for_elements_present(self.start_date_loc)
        self.clear_by_xpath(self.start_date_text_box)
        self.enter_text_field(self.start_date_text_box, start_date_data)

    def select_end_date(self):
        self.wait_for_elements_present(self.end_date_loc)
        self.clear_by_xpath(self.end_date_text_box)
        self.enter_text_field(self.end_date_text_box, end_date_data)

    def click_export_button(self):
        self.click_element(self.export_button)

    def export_data_tabel_is_displayed(self):
        self.assert_element_value(self.export_data_table, export_data_text)

    def working_timing_table(self):
        self.wait_for_elements_present(self.emp_Id_loc)
        emp_id_text = self.get_text_elements(self.emp_Id_data)
        emp_monday_timing_text = self.get_text_elements(self.emp_monday_timing_data)
        emp_tuesday_timing_text = self.get_text_elements(self.emp_tuesday_timing_data)
        emp_wednesday_timing_text = self.get_text_elements(self.emp_wednesday_timing_data)
        emp_thursday_timing_text = self.get_text_elements(self.emp_thursday_timing_data)
        emp_friday_timing_text = self.get_text_elements(self.emp_friday_timing_data)
        data = zip(emp_id_text, emp_monday_timing_text, emp_tuesday_timing_text, emp_wednesday_timing_text,
                   emp_thursday_timing_text, emp_friday_timing_text)
        write_data_to_excel(file_path, data, sheet_name)

    def verify_sending_email_to_employee(self):
        validate_time_sheet(file_path, expected_sheet_name)
        results = validate_and_get_email(file_path, expected_sheet_name, actual_sheet_name)
        email_sent = send_email(subject, message, from_email, results, username, password)
        if email_sent:
            print("Email sent successfully.")
        else:
            print("Failed to send email.")
