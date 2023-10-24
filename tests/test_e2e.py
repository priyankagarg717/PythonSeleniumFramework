from pytest import fixture, mark
from PythonSeleniumFramework.pageObjects.HomePage import HomePage
from PythonSeleniumFramework.testData.OrderData import OrderData
from PythonSeleniumFramework.utilities.BaseClass import BaseClass


class TestCases(BaseClass):

    @fixture(params=[(["Blackberry", "iphone X"], "ind", "India"), (["Nokia Edge"], "chi", "China")])
    def get_data(self, request):
        return request.param

    @fixture(params=OrderData.order_test_data)
    def get_data_dict(self, request):
        return request.param

    @fixture()
    def open_application(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/shop")

    @mark.skip
    def test_e2e(self, open_application, get_data):
        self.driver.implicitly_wait(5)
        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_item()
        print(get_data[0])
        self.add_items_to_cart(checkout_page, get_data[0])
        confirmation_page = checkout_page.click_checkout_button()
        confirmation_page.click_checkout_button()
        confirmation_page.get_deliver_location_field().send_keys(get_data[1])
        self.verify_link_presence(get_data[2])
        confirmation_page.select_delivery_location(get_data[2])
        confirmation_page.select_agree_checkbox()
        confirmation_page.click_purchase_button()
        assert "Success! Thank you!" in confirmation_page.get_success_message()

    def test_e2e_1(self, open_application, get_data_dict):
        self.driver.implicitly_wait(5)
        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_item()
        self.add_items_to_cart(checkout_page, get_data_dict["items"])
        confirmation_page = checkout_page.click_checkout_button()
        confirmation_page.click_checkout_button()
        confirmation_page.get_deliver_location_field().send_keys(get_data_dict["search_location"])
        self.verify_link_presence(get_data_dict["country"])
        confirmation_page.select_delivery_location(get_data_dict["country"])
        confirmation_page.select_agree_checkbox()
        confirmation_page.click_purchase_button()
        assert "Success! Thank you!" in confirmation_page.get_success_message()

    def add_items_to_cart(self, checkout_page, items):
        cards = checkout_page.get_card_titles()

        i = -1
        for card in cards:
            i = i + 1
            card_text = card.text
            print(card_text)
            if card_text in items:
                self.log.info(card_text)
                checkout_page.get_card_footer()[i].click()
