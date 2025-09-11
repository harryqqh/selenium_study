from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_test import BaseTest
import pytest
from time import sleep

class DasboardPage:
        PROFILE = (By.XPATH, "//*[@class='oxd-userdropdown-name']")
        def __init__(self, driver):
            self.driver = driver
        
        def verify_login_successful(self):
            profile = self.driver.find_element(*self.PROFILE)
            return profile.is_displayed()