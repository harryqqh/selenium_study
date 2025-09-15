"""
    Class representing the login page of OrangeHRM.
    Provides methods to interact with the login page.
    """
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    
    USERNAME_INPUT = (By.XPATH, "//*[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//*[@name='password']")
    LOGINBTN = (By.XPATH, "//button[@type='submit']")
        
    def __init__(self, driver):
        super().__init__(driver)
       
    def login(self, user_name, password):
        
        #Perform login actions
        username_field = self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
        password_field = self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT))
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGINBTN))
        
        username_field.send_keys(user_name)
        password_field.send_keys(password)
        login_button.click()
            
               
            

       
    