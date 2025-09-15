from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class VacancyPage(BasePage):
    ADD_BUTTON = (By.XPATH, '//*[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Method to click Add button
    def click_add_button(self):
        add_button = self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON))
        add_button.click()
