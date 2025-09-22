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
        # Perform login action
    def login(self, user_name, pass_word):
        self.get_element(self.USERNAME_INPUT).send_keys(user_name)
        self.get_element(self.PASSWORD_INPUT).send_keys(pass_word)
        self.click(self.LOGINBTN)

            
               
            

       
    