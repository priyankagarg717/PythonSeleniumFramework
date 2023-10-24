from selenium.webdriver.common.by import By

from PythonSeleniumFramework.pageObjects.ConfirmationPage import ConfirmationPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    card_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer_button = (By.CSS_SELECTOR, ".card-footer button")
    checkout_button = (By.PARTIAL_LINK_TEXT, "Checkout")

    def get_card_titles(self):
        return self.driver.find_elements(*self.card_title)

    def get_card_footer(self):
        return self.driver.find_elements(*self.card_footer_button)

    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()
        return ConfirmationPage(self.driver)

