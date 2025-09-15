from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_test import BaseTest
from base.base_page import BasePage
from pages.login_page import LoginPage
from pages.dashboard_page import DasboardPage
from pages.recruitment_page import RecruitmentPage
from pages.vacancy_page import VacancyPage

import pytest

class TestLogin(BaseTest):

        def test_login_ora(self):
            print("🔵 Starting login test")
            # Call login page
            loginpage = LoginPage(self.driver)
        
            #Perform actions
            loginpage.login("Admin", "admin123")

            
            #Verify login successful
            dashboardpage = DasboardPage(self.driver)
            assert dashboardpage.verify_login_successful() == True
            print("✅ Login successful")
            
            # Navigate to Recruitment page
        def test_navigate_to_recruitment(self):
            print("🔵 Starting navigation to Recruitment page test")
            
            recruitment_page = RecruitmentPage(self.driver)
            recruitment_page.navigate_to_recruitment()
            
            # Verify navigation successful by checking the presence of a unique element on the Recruitment page
            assert recruitment_page.verify_navigation_successful() == True
            print("✅ Navigation to Recruitment page successful")
        
        def test_navigate_to_vacancy_and_add(self):
            print('🔵 Starting navigation to Vacancy page and click Add button test')
              # Call Vacancy page
            recruitment_page = RecruitmentPage(self.driver)
            recruitment_page.go_to_vacancy_page()
            
            # Verify Vacancy page navigation successful
            vacancy_page = RecruitmentPage(self.driver)
            assert vacancy_page.verify_vacancy_navigtion_successful() == True
            print("✅ Navigation to Vacancy page successful")
            
            # Call click Add button method
            vacancy_page = VacancyPage(self.driver)
            vacancy_page.click_add_button()
            print("✅ Click Add button successful")
