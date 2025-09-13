import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    #Initialize webdriver
    def setup(self, request):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        request.cls.driver = driver
        self.wait = WebDriverWait(driver,10)
        yield
        driver.quit()