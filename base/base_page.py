from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    #Method to find element
    def get_element(self, xpath):
        element = self.wait.until(EC.presence_of_element_located(xpath))
        return element
    
    #Method to click button element
    def click(self, xpath):
        self.wait.until(EC.presence_of_element_located(xpath)).click()
        
    #Method to input text
    def send_keys(self, xpath, text):
        self.wait.until(EC.presence_of_element_located(xpath)).send_keys(text)

    #Method select dropdown
    def select_dropdown(self, element: tuple, text: str):
        dropdown = self.wait.until(EC.element_to_be_clickable(element))
        select = Select(dropdown)
        select.select_by_visible_text(text)
        
    #Method select span element using javascripts    
    def select_span_using_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)