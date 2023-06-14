from pytest_bdd import parsers, when, given, then

from lib.browser.pages.login_page import Login_page
from lib.browser.pages.my_profile_page import MyProfile_page


@then('validate user can view the their profile on the my profile page.')
def validate_profile_detail(browser):
    my_profile_page = MyProfile_page(browser)
    my_profile_page.click_my_profile_link()
