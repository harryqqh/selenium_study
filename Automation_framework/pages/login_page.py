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
from utils.common import enter_text
import pytest
from time import sleep

class LoginPage:
    @pytest.fixture(scope="class", autouse=True)
    #Initialize webdriver
    def setup(self, request):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        request.cls.driver = driver
        sleep(3)
        yield
        driver.quit()
             
    '''def navigate_to_homepage(self):
        """Load the login page."""
        print(f"Navigating to homepage: {self.base_url}")
        self.driver.get(self.base_url)'''
        
        
    def login(self, username, password):
        """Perform the complete login action."""
        USERNAME_INPUT = (By.XPATH, "//*[@name='username']")
        PASSWORD_INPUT = (By.XPATH, "//*[@name='password']")
        LOGINBTN = (By.XPATH, "//button[@type='submit']")
        
        
        username = self.driver.find_element(*USERNAME_INPUT)
        password = self.driver.find_element(*PASSWORD_INPUT)
        login_button = self.driver.find_element(*LOGINBTN)
        
        #Input username and password
        enter_text(self.wait, USERNAME_INPUT, username)
        enter_text(self.wait, PASSWORD_INPUT, password)
        login_button.click()
    
    def verify_login_successful(self):
        #verify login successful by checking presence of profile element
        self.wait.until(EC.presence_of_element_located(self.profile))
        profile = self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
        assert profile.is_displayed()
        
        
       
        
            
               
            

       
    