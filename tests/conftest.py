import self
from pytest import fixture
from selenium import webdriver

from PythonSeleniumFramework.utilities.BaseClass import BaseClass


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser can be chrome/edge/firefox")
    parser.addoption("--env", action="store", default="qa", help="env can be dev/qa/sat/prod")


def invoke_browser(request):
    browser = request.config.getoption("--browser")
    env = request.config.getoption("--env")
    print(env)
    if 'firefox'.lower() in browser:
        return webdriver.Firefox()
    elif "edge".lower() in browser:
        return webdriver.Edge()
    else:
        return webdriver.Chrome()


@fixture(autouse=True, scope="class")
def setup(request):
    driver = invoke_browser(request)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    request.cls.driver = driver
    yield
    driver.close()


@fixture(autouse=True, scope='class')
def get_logger(request):
    log = BaseClass.get_logger(self)
    request.cls.log = log
