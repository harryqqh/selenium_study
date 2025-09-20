from selenium import webdriver
from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DasboardPage
import pytest

class TestLogin(BaseTest):
    
        # @pytest.mark.smoke # Marking test suites
        
        def test_login_orange(self):
            print("🔵 Starting login test")
            # Initialize page objects
            loginPage = LoginPage(self.driver)
            dashboardPage = DasboardPage(self.driver)
        
            #Perform actions
            print("🔵 Login attempt")
            loginPage.login("Admin", "admin123")

            #Verify login successful
            assert dashboardPage.verify_login_successful() is True
            print("✅ Login successful")
            
     
            
   
