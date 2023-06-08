import random
import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class BasicActions:

    def __init__(self, web_driver):
        self.web_elements = None
        self.text = None
        self.title = None
        self.web_element = WebElement
        self.web_driver = web_driver

    def find_elements(self, locator):
        self.web_driver.find_elements(By.XPATH, locator)

    def click_element(self, locator):
        try:
            self.web_element = self.web_driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            print("No Such element")
        finally:
            try:
                WebDriverWait(self.web_driver, 10). \
                    until(expected_conditions.element_to_be_clickable(self.web_element))
                self.web_element.click()
            except Exception as error:
                print(error)

    def enter_text_field(self, locator, value):
        try:
            self.web_element = self.web_driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            print("No Such element")
            assert False
        finally:
            try:
                WebDriverWait(self.web_driver, 10).until(expected_conditions.element_to_be_clickable(self.web_element))
                self.web_element.send_keys(value)
            except Exception as error:
                print(error)

    def clear_by_xpath(self, locator):
        try:
            self.web_element = self.web_driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            print("No Such element")
            assert False
        finally:
            try:
                WebDriverWait(self.web_driver, 10).until(expected_conditions.element_to_be_clickable(self.web_element))
                self.web_element.clear()
            except Exception as error:
                print(error)

    def select_by_xpath(self, locator, value):
        try:
            self.web_element = self.web_driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            print("No Such element")
            assert False
        finally:
            try:
                WebDriverWait(self.web_driver, 10).until(expected_conditions.element_to_be_clickable(self.web_element))
                select = Select(self.web_element)
                select.select_by_visible_text(value)
            except Exception as error:
                print(error)

    def get_text_element(self, locator):
        text = None
        try:
            self.web_element = self.web_driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            print("No Such element")
            assert False
        finally:
            try:
                text = self.web_element.text

            except Exception as error:
                print(error)
        return text

    def scroll_element(self, locator):

        try:
            self.web_element = self.web_driver.find_element(By.XPATH, locator)
        except NoSuchElementException:
            print("No Such element")
            assert False
        finally:
            try:
                WebDriverWait(self.web_driver, 10).until(expected_conditions.element_to_be_clickable(self.web_element))
                action = ActionChains(self.web_driver)
                action.move_to_element(self.web_element).perform()
            except Exception as error:
                print(error)

    def get_title(self):
        self.title = self.web_driver.title
        return self.title

    def get_text_elements(self, locator):
        list_text = []
        web_elements = None
        try:
            web_elements = self.web_driver.find_elements(By.XPATH, locator)
        except NoSuchElementException:
            print("No Such element")
            assert False
        finally:
            try:
                if len(web_elements) > 1:
                    for web_element in web_elements:
                        self.web_element = web_element
                        self.text = self.web_element.text
                        list_text.append(self.text)
                else:
                    self.web_element = self.web_driver.find_element(By.XPATH, locator)
                    self.text = self.web_element.text
                    list_text.append(self.text)

            except Exception as error:
                print(error)
            return list_text

    def element_is_displayed(self, locator):
        self.web_element = self.web_driver.find_element(By.XPATH, locator)
        return self.web_element.is_displayed()

    def navigate_back(self):
        self.web_driver.back()

    def scroll_down(self):
        self.web_driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def refresh(self):
        self.web_driver.refresh()

    def get_url(self, url):
        self.web_driver.get(url)

    def wait_element(self, wait_time):
        self.web_driver.implicitly_wait(wait_time)

    def find_elements_to_random_click(self, locator, count):
        web_elements = self.web_driver.find_elements(By.XPATH, locator)
        random_products = random.sample(web_elements, count)
        for product in random_products:
            product.click()

    def scroll_to_element_by_text(self, text_element):
        element = self.web_driver.find_element(By.XPATH, f"//*[text()={text_element}]")
        self.web_driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_add_cart_by_product_price(self, text):
        element = self.web_driver.find_element(By.XPATH,
                                               f"//div[text() = {text}]/following-sibling::button[@class='btn "
                                               f"btn_primary btn_small btn_inventory']")
        element.click()

    def verify_textbox(self, locator, expected_value):
        first_name_element = self.web_driver.find_element(By.XPATH, locator)
        entered_value = first_name_element.get_attribute("value")
        assert entered_value == expected_value, \
            f"Validation failed. Expected: {expected_value}, Actual: {entered_value}"

        print(f"Expected: {entered_value} , Actual: {expected_value}")

    def verify_locator_text(self, locator, expected_value):
        first_name_element = self.web_driver.find_element(By.XPATH, locator)
        entered_value = first_name_element.text
        assert entered_value == expected_value, f"Validation failed. Expected: {expected_value}, Actual: {entered_value}"
        print(f"Expected: {entered_value} , Actual: {expected_value}")

    def click_list_button(self, locator):
        list_text = []
        web_elements = self.web_driver.find_elements(By.XPATH, locator)
        if len(web_elements) > 1:
            for web_element in web_elements:
                self.web_element = web_element
                self.text = self.web_element.text
                list_text.append(self.text)

            product_title = list_text
            updated_Xpath = self.web_driver.find_element(By.XPATH, f"//h5[contains(text(),'{product_title}')]")
            updated_Xpath.click()
            self.wait_element(10)
            removed_element = self.web_driver.find_element(By.XPATH,
                                                           "//*[@id='Modal_local_3']/div/div/div[1]/button/span")
            removed_element.click()
            if not removed_element:
                print(f"Your'{product_title}'product is removed from the Cart")
            else:
                print("Something went wrong. Product was not removed.")

    @staticmethod
    def verify_string_text(Expected, Actual):
        expected_value = Expected.strip()
        actual_value = Actual.split(":", 1)[1].strip()
        assert expected_value == actual_value, f"Validation failed. Expected: {expected_value}, Actual: {actual_value}"
        print(f"Expected: {expected_value} , Actual: {actual_value}")
