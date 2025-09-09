from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_login_ora():
    try:
        #access the url
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        #wait for the login page to load
        wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='company-branding']")))
   
    
        #input username and password
        username = driver.find_element(By.XPATH, "//*[@name='username']")
        password = driver.find_element(By.XPATH, "//*[@name='password']")
    
        username.send_keys("Admin")
        password.send_keys("admin123")
    
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
    
        #Wait for loading
        wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='oxd-userdropdown-name']")))
    
        #Verify login successful by checking for profile element
        profile = driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
        assert profile.is_displayed()
        print("✅ Login successful, test completed")
        
    except Exception as e:
        print(f"❌ test failed with error as {e}.")
        
    finally:
        #clowse the browser
        driver.quit()
        print("🔒 Browser closed.")
