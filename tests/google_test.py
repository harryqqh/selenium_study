from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import csv
def read_csv_data(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row['keyword'] for row in reader]
    
#call function   
test_data = read_csv_data('test_data.csv')

# to search keyword in Google

@pytest.mark.parametrize("keyword", test_data)
def test_google(keyword):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keyword)
    search_box.submit()
    # Assert that the keyword appears in the page source (indicating results are shown)
    assert keyword.lower() in driver.page_source.lower(), f"Keyword '{keyword}' not found in page source"

    driver.quit()
