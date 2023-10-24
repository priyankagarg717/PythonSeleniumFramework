from pytest import fixture
from PythonSeleniumFramework.utilities.BaseClass import BaseClass
from PythonSeleniumFramework.testData.OrderData import OrderData


class TestDemo(BaseClass):
    @fixture(params=OrderData.order_excel_data)
    def get_excel_data(self, request):
        return request.param

    def test_demo_1(self):
        log = self.get_logger()
        log.info("Hello. I am demo test1")

    def test_demo_2(self):
        log = self.get_logger()
        log.info("Hello. I am demo test2")

    def test_demo_3(self, get_excel_data):
        log = self.get_logger()
        log.info(get_excel_data['items'])
        log.info(get_excel_data['Country'])
