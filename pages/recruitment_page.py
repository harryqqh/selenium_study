from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class RecruitmentPage(BasePage):
    RECRUITMENT_MENU = (By.XPATH, "//span[text()='Recruitment']")
    HEADER = (By.XPATH, "//h6[contains(@class,'header')]")
    VACANCY = (By.XPATH, "//a[text()='Vacancies']")
    VACANCIES_HEADER = (By.XPATH, '//h5[@class="oxd-text oxd-text--h5 oxd-table-filter-title"]')
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    # Method to navigate to Recruitment page
    def navigate_to_recruitment(self):
        """Navigate to the Recruitment page."""
        self.wait.until(EC.element_to_be_clickable(self.RECRUITMENT_MENU)).click()
        
        
    # Method to verify navigation successful   
    def verify_navigation_successful(self):
        """Verify if navigation to Recruitment page is successful."""
        header = self.wait.until(EC.presence_of_element_located(self.HEADER))
        return header.is_displayed()
    
    # Method to go to Vacancy page
    def go_to_vacancy_page(self):
        self.wait.until(EC.element_to_be_clickable(self.VACANCY)).click()
        
    # Method to verify Vacancy page navigation successful
    def verify_vacancy_navigtion_successful(self):
        vacancies = self.wait.until(EC.presence_of_element_located(self.VACANCIES_HEADER))
        return vacancies.is_displayed()
        