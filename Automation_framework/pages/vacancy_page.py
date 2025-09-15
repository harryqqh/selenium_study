from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class VacancyPage(BasePage):
    ADD_BUTTON = (By.XPATH, '//*[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
    VACANCY_NAME = (By.XPATH,'//label[contains(text(), "Vacancy Name")]/../../div//input')
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Method to click Add button
    def click_add_button(self):
        add_button = self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON))
        add_button.click()
        
    # Method to fill vacancy form
    def fill_vacancy_form(self, vacancy_name):
        vacancyName_field = self.wait.until(EC.presence_of_element_located(self.VACANCY_NAME))
        vacancyName_field.send_keys(vacancy_name)
        