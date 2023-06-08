import time

from selenium.webdriver.common.by import By

from lib.browser.pages.driver_commands import BasicActions
from lib.util.constants import *
from lib.util.excelhandling import *


class OpenPosition_Page(BasicActions):

    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.open_position_link_Xpath = "//span[normalize-space()='Open Positions']"
        self.open_position_page_Xpath = "//h4[@class='page-title']"
        self.job_position_Xpath = "//thead/tr/th[1] | //tr[@role='row']/td[1]"
        self.job_contact_Xpath = "//thead/tr/th[2] | //tr[@role='row']/td[2]"
        self.job_experience_Xpath = "//thead/tr/th[3] | //tr[@role='row']/td[3]"
        self.job_status_Xpath = "//thead/tr/th[4] | //tr[@role='row']/td[4]"
        self.position_title_Xpath = "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[25]/div/div/div[2]/p[1]/text()"
        self.contact_title_Xpath = "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[25]/div/div/div[2]/p[7]/text()"
        self.position_link_Xpath = "(//tr[@role='row']/td[1]/a)"
        self.back_button_Xpath = "(//*[@class='modal-dialog']/div/div/button/span)"
        self.position_text_Xpath = "(//*[@class='modal-body']/p[1])"

    def click_open_position(self):
        self.wait_element(10)
        self.click_element(self.open_position_link_Xpath)

    def verify_open_position_page(self):
        self.wait_element(10)
        open_position_title_text = self.get_text_element(self.open_position_page_Xpath)
        print("Open Positions page :", open_position_title_text)
        self.verify_locator_text(self.open_position_page_Xpath, "Open Positions")

    def open_position_table(self):
        self.wait_element(10)
        job_position = self.get_text_elements(self.job_position_Xpath)
        job_contact = self.get_text_elements(self.job_contact_Xpath)
        job_experience = self.get_text_elements(self.job_experience_Xpath)
        job_status = self.get_text_elements(self.job_status_Xpath)

        data = zip(job_position, job_contact, job_experience, job_status)
        create_excel_sheet(path_file_excel)
        write_data_to_excel(path_file_excel, data, "Open Position")
        read_data_from_excel(path_file_excel)

    def verify_job_position(self):
        self.wait_element(10)
        job_position_Xpath = self.web_driver.find_elements(By.XPATH, self.position_link_Xpath)
        button_count = len(job_position_Xpath)
        print(button_count)
        for button in range(1, button_count):
            position_updated_Xpath = self.web_driver.find_element(By.XPATH, f"{self.position_link_Xpath}{[button]}")
            position_updated_Xpath.click()
            element_text = position_updated_Xpath.get_attribute("text")

            time.sleep(1)
            open_position_title_text = self.get_text_element(f"{self.position_text_Xpath}{[button]}")
            self.verify_string_text(element_text, open_position_title_text)

            time.sleep(1)
            back_button_updated_Xpath = self.web_driver.find_element(By.XPATH,
                                                                     f"{self.back_button_Xpath}{[button]}")
            back_button_updated_Xpath.click()
