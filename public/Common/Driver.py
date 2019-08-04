from selenium import webdriver
from public.pages import BasePage
import time

class Driver(BasePage):
    """
    实例化driver
    """

    def __init__(self,selenium_driver):
        try:
            self.driver = selenium_driver
            self.driver.maximize_window()
            self.wait(3)
        except Exception:
            raise NameError("Not Chrome")

if __name__ == '__main__':
    driver = webdriver.Chrome()
    D = Driver(driver)