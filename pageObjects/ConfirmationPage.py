from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
    delivery_location_textbox = (By.CSS_SELECTOR, "input#country")
    agree_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_button = (By.CSS_SELECTOR, "input[value='Purchase']")
    success_message = (By.CSS_SELECTOR, "[class*='alert-success']")

    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()

    def get_deliver_location_field(self):
        return self.driver.find_element(*self.delivery_location_textbox)

    def select_agree_checkbox(self):
        self.driver.find_element(*self.agree_checkbox).click()

    def click_purchase_button(self):
        self.driver.find_element(*self.purchase_button).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text

    def select_delivery_location(self, location):
        self.driver.find_element(By.LINK_TEXT, location).click()
