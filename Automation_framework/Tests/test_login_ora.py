from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DasboardPage
from time import sleep
import pytest

class TestLogin(BaseTest):
    
    def test_login_ora(self):
        loginpage = LoginPage(self.driver)
        #Perform actions
        loginpage.login("Admin", "admin123")
        print("✅ Login attempted")
        
        #Loading wait
        sleep(5)
        
        #Verify login successful
        dashboardpage = DasboardPage(self.driver)
        assert dashboardpage.verify_login_successful() == True
        print("✅ Login successful, test completed")
    