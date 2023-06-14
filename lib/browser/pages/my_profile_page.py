from lib.browser.pages.driver_commands import BasicActions


class MyProfile_page(BasicActions):

    def __init__(self, web_driver):
        super().__init__(web_driver)


    def click_my_profile_link(self):
        self.wait_for_elements_present(self.my_profile_link_loc)
        self.click_element(self.my_profile_link)
