from lib.util.constants import *
from lib.util.utilities import utilities
from selenium.webdriver.common.by import By

from lib.browser.pages.driver_commands import BasicActions
from lib.data.loginpage_data import *


class Login_page(BasicActions):

    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.login_page = []

    # Locator
    email_textbox_loc = (By.XPATH, "//input[@name='email']")
    login_page_text_loc = (By.XPATH, "//span[normalize-space()='Welcome to Aspire']")
    password_textbox_loc = (By.XPATH, "//input[@name='password']")
    login_button_loc = (By.XPATH, "//input[@id='submitbtn']")
    captcha_textbox_loc = (By.XPATH, "//div[@class='recaptcha-checkbox-border']")
    home_page_loc = (By.XPATH, "//span[normalize-space()='Dashboard']")

    @property
    def email_text_box(self):
        return self.web_driver.find_element(*self.email_textbox_loc)

    @property
    def password_textbox(self):
        return self.web_driver.find_element(*self.password_textbox_loc)

    @property
    def login_button(self):
        return self.web_driver.find_element(*self.login_button_loc)

    @property
    def home_page_text(self):
        return self.web_driver.find_element(*self.home_page_loc)

    @property
    def login_page_text(self):
        return self.web_driver.find_element(*self.login_page_text_loc)

    def aspire_login_text(self):
        self.wait_for_elements_present(self.login_page_text_loc)
        login_page_title_text = self.get_text_element(self.login_page_text)
        utilities.verify_string_text(login_page_title_text, login_page_title)

    def user_login(self, user_type):
        if user_type in "employee":
            self.wait_for_elements_present(self.email_textbox_loc)
            self.enter_text_field(self.email_text_box, employee_user)
            self.user_password_credentials()
            self.click_login_button()
        elif user_type in "manager":
            self.wait_for_elements_present(self.email_textbox_loc)
            self.enter_text_field(self.email_text_box, manger_user)
            self.user_password_credentials()
            self.click_login_button()
        else:
            print("Enter the valid user type")

    def user_password_credentials(self):
        self.wait_for_elements_present(self.password_textbox_loc)
        self.enter_text_field(self.password_textbox, user_password)

    def click_login_button(self):
        self.click_element(self.login_button)

    def verify_home_page_reload(self):
        self.check_page_reload(dash_board_url)

    def verify_home_page(self):
        self.wait_for_elements_present(self.home_page_loc)
        home_page_text = self.get_text_element(self.home_page_text)
        print("Home page :", home_page_text)
        utilities.verify_string_text(home_page_text, home_page)
