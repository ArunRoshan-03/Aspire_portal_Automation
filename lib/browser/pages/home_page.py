import time

from selenium.webdriver.common.by import By

from lib.browser.pages.driver_commands import BasicActions
from lib.data.timesheet_data import time_sheet_page


class Home_page(BasicActions):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    # Locator
    side_bar_link_loc = (By.XPATH, "//a[@class='sidebar-link']")
    dash_board_link_loc = (By.XPATH, "//span[normalize-space()='Dashboard']")
    my_profile_link_loc = (By.XPATH, "//span[normalize-space()='My Profile']")
    human_resource_link_loc = (By.XPATH, "//span[normalize-space()='Human Resource']")
    time_sheet_link_loc = (By.XPATH, "//span[normalize-space()='Timesheet']")
    time_sheet_page_loc = (By.XPATH, "//h1[@class='pull-left']")
    my_colleague_link_loc = (By.XPATH, "//span[normalize-space()='My Colleague']")
    my_colleague_title_text_loc = (By.XPATH, "//h3[normalize-space()='Know your colleague']")
    open_position_link_loc = (By.XPATH, "//span[normalize-space()='Open Positions']")
    open_position_page_loc = (By.XPATH, "//h4[@class='page-title']")
    reimbursements_link_loc = (By.XPATH, "//span[normalize-space()='Reimbursements']")
    reimbursements_title_text_loc = (By.XPATH, "//h4[normalize-space()='My Reimbursements']")
    events_link_loc = (By.XPATH, "//span[normalize-space()='Events']")
    forums_link_loc = (By.XPATH, "//span[normalize-space()='Forums']")
    human_resource_title_loc = (By.XPATH, "//b[normalize-space()='Human Resource Dashboard']")

    # Path
    side_bar_path = "//span[normalize-space()='{}']"

    @property
    def side_bar_link(self):
        return self.web_driver.find_elements(*self.side_bar_link_loc)

    @property
    def dash_board_link(self):
        return self.web_driver.find_element(*self.dash_board_link_loc)

    @property
    def my_profile_link(self):
        return self.web_driver.find_element(*self.my_profile_link_loc)

    @property
    def my_profile_page_text(self):
        return self.web_driver.find_element(*self.my_profile_title_text_loc)

    @property
    def human_resource_link(self):
        return self.web_driver.find_element(*self.human_resource_link_loc)

    @property
    def human_resource_page_title_link(self):
        return self.web_driver.find_element(*self.human_resource_title_loc)

    @property
    def time_sheet_link(self):
        return self.web_driver.find_element(*self.time_sheet_link_loc)

    @property
    def time_sheet_page(self):
        return self.web_driver.find_element(*self.time_sheet_page_loc)

    @property
    def my_colleague_link(self):
        return self.web_driver.find_element(*self.my_colleague_link_loc)

    @property
    def my_colleague_page_text(self):
        return self.web_driver.find_element(*self.my_colleague_title_text_loc)

    @property
    def open_position_link(self):
        return self.web_driver.find_element(*self.open_position_link_loc)

    @property
    def open_position_page_title(self):
        return self.web_driver.find_element(*self.open_position_page_loc)

    @property
    def reimbursements_link(self):
        return self.web_driver.find_element(*self.reimbursements_link_loc)

    @property
    def reimbursements_page_text(self):
        return self.web_driver.find_element(*self.reimbursements_title_text_loc)

    @property
    def events_link(self):
        return self.web_driver.find_element(*self.events_link_loc)

    @property
    def forums_link(self):
        return self.web_driver.find_element(*self.forums_link_loc)

    def verify_side_bar_link(self):
        for side_bar_count in self.side_bar_link:
            self.element_is_displayed(side_bar_count)

    def click_dash_board_link(self):
        self.click_element(self.dash_board_link)
        print(self.page_title())

    def click_human_resources_link(self):
        self.wait_for_elements_present(self.human_resource_link_loc)
        self.click_element(self.human_resource_link)
        self.wait_for_elements_present(self.human_resource_title_loc)
        self.assert_element_value(self.human_resource_page_title_link, 'Human Resource Dashboard')

    def click_my_profile_link(self):
        self.wait_for_elements_present(self.my_profile_link_loc)
        self.click_element(self.my_profile_link)
        print(self.page_title())

    def click_reimbursements_link(self):
        self.wait_for_elements_present(self.reimbursements_link_loc)
        self.click_element(self.reimbursements_link)
        self.wait_for_elements_present(self.reimbursements_title_text_loc)
        self.assert_element_value(self.reimbursements_page_text, 'My Reimbursement')

    def click_my_colleague_link(self):
        self.wait_for_elements_present(self.my_colleague_link_loc)
        self.click_element(self.my_colleague_link)
        self.wait_for_elements_present(self.my_colleague_title_text_loc)
        self.assert_element_value(self.my_colleague_page_text, 'Know your colleague')

    def click_time_sheet_link(self):
        self.wait_for_elements_present(self.time_sheet_link_loc)
        self.click_element(self.time_sheet_link)
        self.wait_for_elements_present(self.time_sheet_page_loc)
        self.assert_element_value(self.time_sheet_page, time_sheet_page)
        self.navigate_back()

    def click_open_position_link(self):
        self.wait_for_elements_present(self.open_position_link_loc)
        self.click_element(self.open_position_link)
        self.wait_for_elements_present(self.open_position_page_loc)
        self.element_is_displayed(self.open_position_page_title)

    def click_event_link(self):
        self.wait_for_elements_present(self.events_link_loc)
        self.click_element(self.events_link)
        print(self.page_title())

    def click_forum_link(self):
        self.wait_for_elements_present(self.forums_link_loc)
        self.click_element(self.forums_link)
        print(self.page_title())

    def verify_side_bar_page(self):
        self.click_dash_board_link()
        self.click_human_resources_link()
        self.click_my_profile_link()
        self.click_reimbursements_link()
        self.click_my_colleague_link()
        self.click_time_sheet_link()
        self.click_open_position_link()
        self.click_event_link()
        self.click_forum_link()
