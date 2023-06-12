import re
import time

from selenium.webdriver.common.by import By

from lib.browser.pages.driver_commands import BasicActions
from lib.data.timesheet_data import *
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
        self.enter_saturday_timings(common_timing)
        self.enter_sunday_timings(common_timing)

    def click_activity_dropdown_box(self):
        self.click_element(self.activity_drop_down_box)
        self.select_by_xpath(self.activity_option, "Documentation/Reports")

    def click_save_button(self):
        self.wait_for_elements_present(self.save_button_loc)
        self.click_element(self.save_button)
        self.wait_for_elements_present(self.okay_button_loc)
        self.click_element(self.okay_button)

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
