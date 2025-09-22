from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DasboardPage
from pages.recruitment_page import RecruitmentPage
from pages.vacancy_page import VacancyPage
from datetime import datetime

import pytest
   
class TestVacancies(BaseTest):
    
    # @pytest.mark.smoke # Marking test suites 
    
    def test_vacancy_page(self):
        # Initialize page objects
        loginPage = LoginPage(self.driver)
        dashboardPage = DasboardPage(self.driver)
        recruitmentPage = RecruitmentPage(self.driver)
        vacanciesPage = RecruitmentPage(self.driver)
        addVacancyPage = VacancyPage(self.driver)
        
        vacancyName = 'Automation tester for' + str(datetime.now())

        # Perform login
        print("🔵 Login attempt")
        loginPage.login("Admin", "admin123")
        assert dashboardPage.verify_login_successful() is True
        print("✅ Login successful")
        
        # Navigate to Recruitment and Vacancy
        recruitmentPage.navigate_to_recruitment()
        vacanciesPage.go_to_vacancy_page()
        
        # Add new vacancy
        print("🔵 Perform complete add Vacancy")
        addVacancyPage.perform_complete_add_vacancy(vacancyName, "Automation testing is running", "1")
        assert addVacancyPage.verify_edit_vacancy_displayed() is True, 'Failed to add new vacancy'
        print('✅ New Vacancy added successfully')
        
        # Navigate back to Vacancy page
        addVacancyPage.click_cancel_button()
        assert vacanciesPage.verify_vacancy_navigtion_successful() is True
        print("✅ Navigation back to Vacancy page successful")
        
        # Perform Searching Manager
        print("🔵 Perform Searching Hiring Manager")
        addVacancyPage.search_vacancy()