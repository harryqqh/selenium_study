from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
import time

#Set up Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Open URL
driver.get("https://tiki.vn/")

#Wait for the page to load
time.sleep(2)

#Print URL
print(f"Page title is: {driver.current_url}")

#Close the browser
driver.quit()
