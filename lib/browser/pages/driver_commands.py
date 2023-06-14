import random
import time

import polling

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class BasicActions:

    def __init__(self, web_driver):
        self.web_elements = None
        self.text = None
        self.title = None
        self.web_element = WebElement
        self.web_driver = web_driver

    def wait_for_elements_present(self, locator, timeout=10, sleep_interval=0.5):
        try:
            polling.poll(lambda: len(self.web_driver.find_elements(*locator)) > 0, step=sleep_interval, timeout=timeout)
        except polling.TimeoutException:
            assert False

    def get_text_element(self, element):
        self.text = None
        try:
            self.text = element.text
        except NoSuchElementException:
            print("No Such element")
            assert False
        except Exception as error:
            print(error)
        return self.text

    def get_text(self, locator):
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

    def click_element(self, element, timeout=10):
        try:
            self.web_element = element
        except NoSuchElementException:
            print("No Such element")
        finally:
            try:
                WebDriverWait(self.web_driver, timeout).until(EC.element_to_be_clickable(self.web_element))
                self.web_element.click()
            except Exception as error:
                print(error)

    def enter_text_field(self, element, value, timeout=10):
        try:
            WebDriverWait(self.web_driver, timeout).until(EC.element_to_be_clickable(element))
            element.send_keys(value)
        except NoSuchElementException:
            print("No Such element")
            assert False
        except Exception as error:
            print(error)

    def element_is_displayed(self, element, timeout=10):
        try:
            self.web_element = element
            WebDriverWait(self.web_driver, timeout).until(EC.visibility_of(self.web_element))
            assert self.web_element.is_displayed(), "Element is not displayed"
            print(f"'{self.web_element.text}' Elements is displayed")
        except TimeoutException:
            assert False, "Element is not displayed within the specified timeout"
        except AssertionError as e:
            print(f"Assertion Error: {e}")

    def assert_element_value(self, element, expected_value, timeout=10):
        try:
            self.web_element = element
            WebDriverWait(self.web_driver, timeout).until(EC.visibility_of(self.web_element))
            assert self.web_element.is_displayed(), "Element is not displayed"
            actual_value = self.web_element.text
            assert actual_value == expected_value, f"Element value '{actual_value}' does not match expected value '{expected_value}'"
            print(f"Expected: {expected_value} , Actual: {actual_value}")
        except TimeoutException:
            assert False, "Element is not displayed within the specified timeout"
        except AssertionError as e:
            print(f"Assertion Error: {e}")

    @staticmethod
    def get_text_elements(elements):
        texts = []
        for element in elements:
            try:
                texts.append(element.text)
                print(texts)
            except NoSuchElementException:
                print("No Such element")
                assert False
            except Exception as error:
                print(error)
        return texts

    @staticmethod
    def xpath_to_locator(xpath):
        locator = (By.XPATH, xpath)
        return locator

    def xpath_to_locators(self, locator):
        return self.web_driver.find_elements(*locator)

    def wait_for_elements(self, locator, timeout=10):
        WebDriverWait(self.web_driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def wait_for_locator_visible(self, locator, timeout=10):
        WebDriverWait(self.web_driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def wait_for_elements_visible(self, element, timeout=10):
        WebDriverWait(self.web_driver, timeout).until(EC.visibility_of(element))

    def page_reload(self):
        current_url = self.web_driver.current_url
        print(current_url)

    def page_title(self):
        current_title = self.web_driver.title
        return current_title

    def clear_by_xpath(self, element):
        try:
            self.web_element = element
        except NoSuchElementException:
            print("No Such element")
            assert False
        finally:
            try:
                WebDriverWait(self.web_driver, 10).until(
                    expected_conditions.element_to_be_clickable(self.web_element))
                self.web_element.clear()
            except Exception as error:
                print(error)

    def select_by_xpath(self, element, value):
        try:
            self.web_element = element
        except NoSuchElementException:
            print("No Such element")
            assert False
        finally:
            try:
                WebDriverWait(self.web_driver, 10).until(
                    expected_conditions.element_to_be_clickable(self.web_element))
                if self.web_element.tag_name == "select":
                    select = Select(self.web_element)
                    select.select_by_visible_text(value)
                else:
                    self.web_element.click()
                    option_xpath = f"//option[text()='{value}']"
                    option_element = self.web_driver.find_element(By.XPATH, option_xpath)
                    option_element.click()
            except Exception as error:
                print(error)

    def check_page_reload(self, expected_url):
        current_url = self.web_driver.current_url

        if current_url == expected_url:
            print(f"Page has reloaded successfully Url:'{current_url}'")
            return True
        else:
            print(f"Page has not reloaded yetUrl:'{current_url}'")
            return False

    def navigate_back(self):
        self.web_driver.back()
