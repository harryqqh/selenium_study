from selenium import webdriver
from selenium.webdriver.common.by import By
 #wait for username field to be present
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

def test_login_ora():
    
    #access the url
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    
    #wait for loading
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@name='username']")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@name='password']")))
    
    #input username and password
    username = driver.find_element(By.XPATH, "//*[@name='username']")
    password = driver.find_element(By.XPATH, "//*[@name='password']")
    
    username.send_keys("Admin")
    password.send_keys("admin123")
    
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    
    #Wait for loading
    wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='oxd-userdropdown-name']")))
    
    profile = driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
    assert profile.is_displayed()
    
    print(f"Login successful, test completed") 
    
    driver.quit()