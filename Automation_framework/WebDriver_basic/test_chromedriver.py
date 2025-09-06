from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
import time

#Set up Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Open URL
driver.get("https://www.google.com")

#Wait for the page to load
time.sleep(2)

#Print URL
print(f"Page URL is: {driver.current_url}")

#Print title
print(f"Page title is: {driver.title}")

#Find the search box using its name attribute value
search_box = driver.find_element(By.NAME, "q")

#Type in search box
search_box.send_keys("shopee")
search_box.submit()

#Wait for loading
time.sleep(2)

#Print URL
print(f"Page URL is: {driver.current_url}")

#go back and forward
driver.back()
time.sleep(2)
print(f"Page Url is: {driver.current_url}")

driver.forward()
time.sleep(2)
print(f"Page Url is: {driver.current_url}")

#Close the browser
driver.quit()

#End of code
print("Test completed.")
