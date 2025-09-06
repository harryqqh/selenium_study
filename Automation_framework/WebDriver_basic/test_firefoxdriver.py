import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

def test_firefox_launch():
    service = FirefoxService(executable_path="geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    driver.get("https://www.google.com")
    
    