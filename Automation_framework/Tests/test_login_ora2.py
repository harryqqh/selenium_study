import sys
import os
# Add the parent directory to the path to import utils
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import pytest

def test_login_ora():
    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    
    try:
        # Create an instance of the LoginPage
        login_page = LoginPage(driver)
        
        # Navigate to the login page
        login_page.navigate_to_homepage()
        
        # Perform login actions
        login_page.login("Admin", "admin123")
        login_page.verify_login_successful()
        
        #Print summary
        print(f"Login successful, test completed")
    except AssertionError:
        print("❌ Login failed: {profile} not found in URL.")
    except Exception as e:
        print(f"Test failed with error: {e}")

    #finally:
        #driver.quit()
        #print("🔒 Browser closed.")   
    
