import time

from selenium.webdriver.common.by import By

from lib.browser.pages.driver_commands import BasicActions
from lib.data.openpositions_page_data import *
from lib.util.constants import *
from lib.util.utilities import utilities


class OpenPosition_Page(BasicActions):

    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.button_index = None
        self.value = []

    # locator
    open_position_link_loc = (By.XPATH, "//span[normalize-space()='Open Positions']")
    open_position_page_loc = (By.XPATH, "//h4[@class='page-title']")
    job_position_loc = (By.XPATH, "//thead/tr/th[1] | //tr[@role='row']/td[1]")
    job_contact_loc = (By.XPATH, "//thead/tr/th[2] | //tr[@role='row']/td[2]")
    job_experience_loc = (By.XPATH, "//thead/tr/th[3] | //tr[@role='row']/td[3]")
    job_status_loc = (By.XPATH, "//thead/tr/th[4] | //tr[@role='row']/td[4]")
    position_link_loc = (By.XPATH, "(//tr[@role='row']/td[1]/a)")
    cancel_button_loc = (By.XPATH, "//*[@class='modal-dialog']/div/div/button/span")
    position_text_loc = (By.XPATH, "(//*[@class='modal-body']/p[1])")
    alert_table_loc = (By.XPATH, "//*[@class='modal fade']")

    @property
    def open_position_link(self):
        return self.web_driver.find_element(*self.open_position_link_loc)

    @property
    def open_position_page_title(self):
        return self.web_driver.find_element(*self.open_position_page_loc)

    @property
    def list_position_link(self):
        return self.web_driver.find_elements(*self.position_link_loc)

    @property
    def position_text(self):
        return self.web_driver.find_elements(*self.position_text_loc)

    @property
    def cancel_button(self):
        return self.web_driver.find_elements(*self.cancel_button_loc)

    @property
    def position_alert_detail(self):
        return self.web_driver.find_elements(*self.alert_table_loc)

    def verify_open_position_link(self):
        self.element_is_displayed(self.open_position_link)
        self.assert_element_value(self.open_position_link, open_positions_text)

    def click_open_position_link(self):
        self.wait_for_elements_present(self.open_position_link_loc)
        self.click_element(self.open_position_link)

    def open_position_page(self):
        self.wait_for_elements_present(self.open_position_page_loc)
        self.element_is_displayed(self.open_position_page_title)

    def verify_open_position_page_reload(self):
        self.check_page_reload(open_position_sheet_url)

    def verify_open_position_page(self):
        self.wait_for_elements_present(self.open_position_page_loc)
        open_position_title_text = self.get_text_element(self.open_position_page_title)
        print("Open Positions page :", open_position_title_text)
        utilities.verify_string_text(open_position_title_text, open_positions_text)

    def verify_job_positions(self):
        for position_button_count in self.list_position_link:
            self.click_element(position_button_count)
            position_text = position_button_count.get_attribute("text")

            self.wait_for_elements(self.alert_table_loc)
            job_position_elements = self.position_text[self.list_position_link.index(position_button_count)]
            self.wait_for_elements_visible(job_position_elements)
            job_position_text = self.get_text_element(job_position_elements)
            utilities.verify_string_text(position_text, job_position_text)

            cancel_button = self.cancel_button[self.list_position_link.index(position_button_count)]
            self.click_element(cancel_button)

    def open_position_page_reload(self):
        self.page_reload()
