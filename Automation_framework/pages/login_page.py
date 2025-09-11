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
    @pytest.fixture(scope="class", autouse=True)
    
    #Initialize webdriver
    def setup(self, request):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)
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
        username.clear()
        username.send_keys('Admin')
        password.clear()
        password.send_keys('admin123')
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
        login_button.click()
    
    def verify_login_successful(self):
        #verify login successful by checking presence of profile element
        self.wait.until(EC.presence_of_element_located(self.profile))
        profile = self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
        assert profile.is_displayed()'''
       
        
            
               
            

       
    