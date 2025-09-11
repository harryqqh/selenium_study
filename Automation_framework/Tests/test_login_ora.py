from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from time import sleep
import pytest

class TestLogin(LoginPage):
    
    def test_login_ora(self):
        print("🔑 Starting login test")
        #Perform actions
        self.login("Admin", "admin123")
        print("✅ Login attempted")
        
        #Loading wait
        sleep(3)
        
        #Verify login successful by checking for profile element
        profile = self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
        assert profile.is_displayed()
        print("✅ Login successful, test completed")
    