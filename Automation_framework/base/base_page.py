from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    #Wait for element
    def get_element(self, xpath):
        element = self.wait.until(EC.presence_of_element_located(xpath))
        return self.driver.find_element(element)
    
    #Wait for button to clickable
    def click(self, xpath):
        self.wait.until(EC.presence_of_element_located(xpath)).click()
        
    #Method to input text
    def send_keys(self, xpath, text):
        element = self.wait.until(EC.presence_of_element_located(xpath))
        element.send_keys(text)
        
    #Verify if dropdown is selectable
    def select_dropdown(self, element):
        select = self.Select(self.wait.until(EC.presence_of_element_located(element)))
        select.select_by_visible_text('Option 1')
        sleep(2)
        select.select_by_visible_text('Option 2')