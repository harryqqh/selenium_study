from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from base.base_page import BasePage
from time import sleep



class VacancyPage(BasePage):
    
    ADD_BUTTON = (By.XPATH, '//*[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
    HIRING_MANAGER_DROPDOWN = (By.XPATH, '//label[contains(text(),"Hiring Manager")]/parent::div/following-sibling::div//i[contains(@class,"oxd-select-text--arrow")]')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit" and text()=" Search "]')
    
    
    VACANCY_NAME_INPUT = (By.XPATH,'//label[contains(text(), "Vacancy Name")]/../../div//input')
    DESCRIPTION_TEXTAREA = (By.XPATH, '//textarea[@placeholder="Type description here"]')
    HIRING_MANAGER_INPUT = (By.XPATH, '//input[@placeholder="Type for hints..."]')
    NUMBER_OF_POSITIONS_INPUT = (By.XPATH, '//label[contains(text(), "Number of Positions")]/../../div/input')
    PROFILE = (By.XPATH, "//*[@class='oxd-userdropdown-name']")
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')
    JOB_TITLE_DROPDOWN = (By.XPATH,'//div[@class="oxd-select-wrapper"]')
    JOB_TITLE = (By.XPATH,'//div[@role="listbox"]//span[text()= "QA Engineer"]')
    CANCEL_BUTTON = (By.XPATH, '//button[@type="button" and text()=" Cancel "]')
    EDIT_VACANCY_LABEL = (By.XPATH, '//h6[text()="Edit Vacancy"]')

    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
        
    
    # Method to click Add button
    def click_add_button(self):
        add_button = self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON))
        add_button.click()
        
    # Method to fill vacancy form
    def fill_vacancy_name(self, vacancy_name: str):
        self.wait.until(EC.presence_of_element_located(self.VACANCY_NAME_INPUT)).send_keys(vacancy_name)
        
    # Select from dropdown
    def select_job_title_from_dropdown(self):
        self.click(self.JOB_TITLE_DROPDOWN)
        self.wait.until(EC.presence_of_element_located(self.JOB_TITLE)).click()
        
    # Methods to fill description
    def fill_description(self, description: str):
        self.wait.until(EC.presence_of_element_located(self.DESCRIPTION_TEXTAREA)).send_keys(description)
    
    def fill_hiring_manager(self):
        manager = self.get_element(self.PROFILE).text
        input_element = self.get_element(self.HIRING_MANAGER_INPUT)
        self.actions.send_keys_to_element(input_element, manager)\
            .pause(2)\
            .send_keys(Keys.DOWN)\
            .send_keys(Keys.ENTER)\
            .perform()
    
    def fill_number_of_positions(self, number_of_position: int):
        self.wait.until(EC.presence_of_element_located(self.NUMBER_OF_POSITIONS_INPUT)).send_keys(number_of_position)
    
    def click_save_button(self):
        self.get_element(self.SAVE_BUTTON).click()
        
    def verify_edit_vacancy_displayed(self):
        edit_vacancy_label = self.wait.until(EC.presence_of_element_located(self.EDIT_VACANCY_LABEL))
        return edit_vacancy_label.is_displayed()
         
        
    def click_cancel_button(self):
        self.get_element(self.CANCEL_BUTTON).click()
        
    def select_manager_dropdown(self):
        self.get_element(self.HIRING_MANAGER_DROPDOWN).click()
        
    def click_search_button(self):
        self.get_element(self.SEARCH_BUTTON).click()
    
    def select_hiring_manager(self):
        manager = self.get_element(self.PROFILE).text
        manager_locator = (By.XPATH,f"//div[@role='option']//span[text()='{manager}']")
        self.click(manager_locator)


    # Perform complete actions   
    def perform_complete_add_vacancy(self, vacancy_name: str, description: str, number_of_position: int):
           self.click_add_button()
           self.fill_vacancy_name(vacancy_name)
           self.select_job_title_from_dropdown()
           self.fill_description(description)
           self.fill_hiring_manager()
           self.fill_number_of_positions(number_of_position)
           self.click_save_button()
           sleep(1) # for UI showcase
           
    def search_vacancy(self):
        self.select_job_title_from_dropdown()
        self.select_manager_dropdown()
        self.select_hiring_manager()
        self.click_search_button()
        sleep(2) # for UI showcase