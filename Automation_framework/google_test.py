from selenium import webdriver
import pytest
import csv
def read_csv_data(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [row['keyword'] for row in reader]
    
#call funtion   
test_data = read_csv_data('data/test_data.csv')

#to searh keyword in google 
@pytest.mark.parametrize("keyword", test_data)
def test_google_test(keyword):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys(keyword)
    search_box.submit()

    driver.quit()
