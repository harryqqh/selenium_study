from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_test import BaseTest
import time
import pytest

class TestLogin(BaseTest):
    
    def test_login_ora(self):
        USERNAME_INPUT = (By.XPATH, "//*[@name='username']")
        PASSWORD_INPUT = (By.XPATH, "//*[@name='password']")
        LOGINBTN = (By.XPATH, "//button[@type='submit']")
        
        #Access driver from Basetest class
        username = self.driver.find_element(*USERNAME_INPUT)
        password = self.driver.find_element(*PASSWORD_INPUT)
        login_button = self.driver.find_element(*LOGINBTN)
        
        #Perform action
        username.send_keys('Admin')
        password.send_keys('admin123')
        login_button.click()
        
        #Wait for loading
        time.sleep(5) 
        
        #Verify login successful by checking for profile element
        profile = self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
        assert profile.is_displayed()
        print("✅ Login successful, test completed")  
        
