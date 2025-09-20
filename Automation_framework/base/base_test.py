import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options # Import function form library for optional interaction


class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    #Initialize webdriver
    def setup(self, request):
        chrome_options = webdriver.ChromeOptions() # definition option 
        chrome_options.add_argument("--headless") # add option to Run headless (no UI)
        driver = webdriver.Chrome(options=chrome_options) # implement option 
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        request.cls.driver = driver
        self.wait = WebDriverWait(driver,10)
        yield
        driver.quit()