"""
    Class representing the login page of OrangeHRM.
    Provides methods to interact with the login page.
    """
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    
    USERNAME_INPUT = (By.XPATH, "//*[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//*[@name='password']")
    LOGINBTN = (By.XPATH, "//button[@type='submit']")
        
    def __init__(self, driver):
        super().__init__(driver)
       
    def login(self, user_name, password):
        
        #Input username and password
        self.send_keys(self.USERNAME_INPUT, user_name)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGINBTN)
            
               
            

       
    