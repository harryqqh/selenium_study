from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import time
import pytest

class TestLogin(LoginPage):
    
    def test_login_ora(self):
        #Perform actions
        self.login("Admin", "admin123")
        print("✅ Login attempted")
        
        #Wait for loading
        time.sleep(5) 
        
        #Verify login successful by checking for profile element
        profile = self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
        assert profile.is_displayed()
        print("✅ Login successful, test completed")