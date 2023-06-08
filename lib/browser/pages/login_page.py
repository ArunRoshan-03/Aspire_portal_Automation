import time

from lib.browser.pages.driver_commands import BasicActions
from lib.util.excelhandling import create_excel_sheet


class Login_page(BasicActions):

    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.user_email_id_textbox_Xpath = "//input[@name='email']"
        self.login_page_text_Xpath = "//span[normalize-space()='Welcome to Aspire']"
        self.user_password_textbox_Xpath = "//input[@name='password']"
        self.login_button_Xpath = "//input[@id='submitbtn']"
        self.captcha_textbox_Xpath = "//div[@class='recaptcha-checkbox-border']"
        self.home_page_Xpath = "//span[normalize-space()='Dashboard']"

    def aspire_login_text(self):
        self.wait_element(10)
        login_page_title_text = self.get_text_element(self.login_page_text_Xpath)
        print("Login page :", login_page_title_text)
        self.verify_locator_text(self.login_page_text_Xpath, "Welcome to Aspire")

    def user_email_id_credentials(self, user_email):
        self.wait_element(10)
        self.enter_text_field(self.user_email_id_textbox_Xpath, user_email)

    def user_password_credentials(self, password):
        self.wait_element(10)
        self.enter_text_field(self.user_password_textbox_Xpath, password)

    def click_login_button(self):
        self.click_element(self.login_button_Xpath)

    def verify_home_page(self):
        self.wait_element(10)
        home_page_title_text = self.get_text_element(self.home_page_Xpath)
        print("Home page :", home_page_title_text)
        self.verify_locator_text(self.home_page_Xpath, "Dashboard")
