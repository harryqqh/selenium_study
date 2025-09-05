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
time.sleep(3)

#Find element by class name
search_box = driver.find_element(By.CLASS_NAME, "sc-dec0a11d-2 lgENLJ")
search_box.send_keys("Sách lập trình")

#Wait to see the result
time.sleep(5)

#Close the browser
driver.quit()
