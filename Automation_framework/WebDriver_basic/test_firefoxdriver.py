import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

def test_firefox_launch():
    driver = webdriver.Firefox(service=Service(FirefoxDriverManager().install()))
    driver.get("https://www.google.com")
    
    