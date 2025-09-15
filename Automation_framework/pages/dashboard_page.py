from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class DasboardPage(BasePage):
        PROFILE = (By.XPATH, "//*[@class='oxd-userdropdown-name']")
        
        def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)
            
        def verify_login_successful(self):
            profile = self.wait.until(EC.presence_of_element_located(self.PROFILE))
            return profile.is_displayed()