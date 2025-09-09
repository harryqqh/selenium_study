import pytest
from selenium import webdriver
from time import sleep


class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    #Initialize webdriver
    def setup(self, request):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        request.cls.driver = driver
        sleep(3)
        yield
        driver.quit()    