from selenium.webdriver.common.by import By

from PythonSeleniumFramework.pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop_link = (By.LINK_TEXT, "Shop")

    def shop_item(self):
        self.driver.find_element(*self.shop_link).click()
        return CheckoutPage(self.driver)
