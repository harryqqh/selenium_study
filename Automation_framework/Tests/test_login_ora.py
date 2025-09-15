from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DasboardPage
from pages.recruitment_page import RecruitmentPage
from pages.vacancy_page import VacancyPage

import pytest

class TestLogin(BaseTest):
    try:
        def test_login_ora(self):
            print("🔵 Starting login test")
            # Initialize page objects
            loginPage = LoginPage(self.driver)
            dashboardPage = DasboardPage(self.driver)
        
            #Perform actions
            print("🔵 Login attempted")
            loginPage.login("Admin", "admin123")

            #Verify login successful
            assert dashboardPage.verify_login_successful() == True
            print("✅ Login successful")
            
            # Navigate to Recruitment page
        def test_navigate_to_recruitment(self):
            #  Initialize page objects
            recruitmentPage = RecruitmentPage(self.driver)
            
            print("🔵 Starting navigation to Recruitment page test")
            recruitmentPage.navigate_to_recruitment()
            
            # Verify navigation successful by checking the presence of a unique element on the Recruitment page
            assert recruitmentPage.verify_navigation_successful() == True
            print("✅ Navigation to Recruitment page successful")
        
        def test_navigate_to_vacancy_and_add(self):
            print('🔵 Starting navigation to Vacancy page and click Add button test')
              # Initialize page objects
            recruitmentPage = RecruitmentPage(self.driver)
            vacancyPage = RecruitmentPage(self.driver)
            vacanciesPage = VacancyPage(self.driver)
            
            # Navigate to Vacancy page
            print("🔵 Navigating to Vacancy page")
            recruitmentPage.go_to_vacancy_page()
            
            # Verify Vacancy page navigation successful
            assert vacancyPage.verify_vacancy_navigtion_successful() == True
            print("✅ Navigation to Vacancy page successful")
            
            # Call click Add button method
            vacanciesPage.click_add_button()
            print("✅ Click Add button successful")
            
    except Exception as e:
        print(f"❌ An error occurred: {e}")
