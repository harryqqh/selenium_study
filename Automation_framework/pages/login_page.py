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
import pytest
from time import sleep

class LoginPage:
    USERNAME_INPUT = (By.XPATH, "//*[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//*[@name='password']")
    LOGINBTN = (By.XPATH, "//button[@type='submit']")
    
    def __init__(self, driver):
        self.driver = driver
           
    def login(self, user_name, password):
        """Perform the complete login action."""
        #Locate elements
        username_field = self.driver.find_element(*self.USERNAME_INPUT)
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        login_button = self.driver.find_element(*self.LOGINBTN)

        #Input username and password
        username_field.send_keys(user_name)
        password_field.send_keys(password)
        login_button.click()
    
    
    
    
    
    
    
        
    '''class LoginPage:
    
    def __init__(self, driver, base_url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 5)
             
    def navigate_to_homepage(self):
        """Load the login page."""
        print(f"Navigating to homepage: {self.base_url}")
        self.driver.get(self.base_url)
        
        
    def login(self, username, password):
        """Perform the complete login action."""
        username = self.driver.find_element(By.XPATH, "//*[@name='username']")
        password = self.driver.find_element(By.XPATH, "//*[@name='password']")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        enter(self.wait, username, username)
        enter(self.wait, password, password)
        login_button.click()'''
       
        
            
               
            

       
    