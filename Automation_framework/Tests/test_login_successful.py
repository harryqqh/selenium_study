from selenium import webdriver
from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DasboardPage
from utils.config_reader import ConfigReader
import pytest

class TestLogin(BaseTest):
    
        @pytest.mark.smoke # Marking test suites
        
        def test_login_orange(self):
            print("🔵 Starting login test")
            # Initialize page objects
            loginPage = LoginPage(self.driver)
            dashboardPage = DasboardPage(self.driver)
            userName = ConfigReader(self.driver)
            passWord = ConfigReader(self.driver)
            user_name = userName.get_username()
            pass_word = passWord.get_password()
            
            print("🔵 Login attempt")
            loginPage.login(user_name, pass_word)
                       
            

            #Verify login successful
            assert dashboardPage.verify_login_successful() is True
            print("✅ Login successful")
            
     
            
   
