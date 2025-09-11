from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class RecruitmentPage:
    RECRUITMENT_MENU = (By.XPATH, "//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")
    
    def __init__(self, driver):
        self.driver = driver
        
    def navigate_to_recruitment(self):
        """Navigate to the Recruitment page."""
        recruitment_menu = self.driver.find_element(*self.RECRUITMENT_MENU)
        recruitment_menu.click()
        print("✅ Navigated to Recruitment page")