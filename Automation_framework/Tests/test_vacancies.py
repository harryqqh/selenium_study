from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DasboardPage
from pages.recruitment_page import RecruitmentPage
from pages.vacancy_page import VacancyPage

import pytest
   
class TestVacancies(BaseTest):
    def test_vacancy_page(self):
        # Initialize page objects
        loginPage = LoginPage(self.driver)
        dashboardPage = DasboardPage(self.driver)
        recruitmentPage = RecruitmentPage(self.driver)
        vacanciesPage = RecruitmentPage(self.driver)
        addVacancyPage = VacancyPage(self.driver)
        
        # Perform complete acions
        print("🔵 Login attempt")
        loginPage.login("Admin", "admin123")
        assert dashboardPage.verify_login_successful() is True
        print("✅ Login successful")
        recruitmentPage.navigate_to_recruitment()
        assert recruitmentPage.verify_navigation_successful() is True
        print("✅ Navigation to Recruitment page successful")
        vacanciesPage.go_to_vacancy_page()
        assert vacanciesPage.verify_vacancy_navigtion_successful() is True
        print("✅ Navigation to Vacancy page successful")
        print("🔵 Starting Vacancy page test")
        # Add new vacancy
        print("🔵 Perform complete add Vacancy")
        addVacancyPage.perform_complete_add_vacancy('Vacancy Name','Automation Tester', 'this is description', '2')
        print('✅ New Vacancy added successfully')
        
   
   
   
    # Call click Add button method
        #     vacanciesPage.click_add_button()
        #     print("✅ Click Add button successful")