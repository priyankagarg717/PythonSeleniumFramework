from datetime import datetime
import inspect
import logging
import pathlib

from pytest import mark
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# @mark.usefixtures("setup")
class BaseClass:

    def verify_link_presence(self, link_text):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, link_text))
        )

    def get_logger(self):
        log_path = pathlib.Path.cwd() / "logs"
        # log_path.mkdir(parents=True, exist_ok=True)
        filename = str(log_path / f"{datetime.now(): %Y-%m-%d_%H-%M-%S}_logs.log")
        print(filename)
        testcasename = inspect.stack()[1][3]
        logger = logging.getLogger(testcasename)
        file_handler = logging.FileHandler(filename)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # file_handler object
        logger.setLevel(logging.INFO)
        return logger