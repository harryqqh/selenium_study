from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DasboardPage
from pages.recruitment_page import RecruitmentPage

import pytest

class TestRecruitment(BaseTest):
    
    def test_navigate_to_recruitment(self):
        # Initialize page objects
        loginPage = LoginPage(self.driver)
        dashboardPage = DasboardPage(self.driver)
        recruitmentPage = RecruitmentPage(self.driver)
        vacancyPage = RecruitmentPage(self.driver)
        
        # Perform complete acions
        print("🔵 Login attempt")
        loginPage.login("Admin", "admin123")
        assert dashboardPage.verify_login_successful() is True
        print("✅ Login successful")
        
        print("🔵 Starting navigation to Recruitment page test")
        recruitmentPage.navigate_to_recruitment()
        
        # Verify navigation successful
        assert recruitmentPage.verify_navigation_successful() is True
        print("✅ Navigation to Recruitment page successful")
        
        # Navigate to Vacancy page
        print("🔵 Navigating to Vacancy page")
        vacancyPage.go_to_vacancy_page()
        
        # Verify Vacancy page navigation successful
        assert vacancyPage.verify_vacancy_navigtion_successful() is True
        print("✅ Navigation to Vacancy page successful")
