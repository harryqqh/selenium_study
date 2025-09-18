from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from base.base_page import BasePage

class VacancyPage(BasePage):
    ADD_BUTTON = (By.XPATH, '//*[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
    VACANCY_NAME_INPUT = (By.XPATH,'//label[contains(text(), "Vacancy Name")]/../../div//input')
    JOB_TITLE_DROPDOWN =(By.XPATH,'//*[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]')
    DESCRIPTION_TEXTAREA = (By.XPATH, '//textarea[@placeholder="Type description here"]')
    HIRING_MANAGER_INPUT = (By.XPATH, '//input[@placeholder="Type for hints..."]')
    NUMBER_OF_POSITIONS_INPUT = (By.XPATH, '//label[contains(text(), "Number of Positions")]/../../div/input')
    PROFILE = (By.XPATH, "//*[@class='oxd-userdropdown-name']")
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')
    
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
    def select_from_dropdown(self):
        #Click to open dropdown
        self.wait.until(EC.element_to_be_clickable((self.JOB_TITLE_DROPDOWN))).click()
        
    def select_job_tiltle(self, job_title: str):
        #Select option
        job_title_option_xpath = f'//div[@class="oxd-select-wrapper"]//div[@role="listbox"]//div[text()={job_title}]'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, job_title_option_xpath))).click()
    
    # Methods to fill description
    def fill_description(self, description: str):
        self.wait.until(EC.presence_of_element_located(self.DESCRIPTION_TEXTAREA)).send_keys(description)
    
    def fill_hiring_manager(self):
        manager = self.get_element(self.PROFILE).text
        self.actions.send_keys_to_element(self.HIRING_MANAGER_INPUT,manager).pause(1).send_keys(Keys.DOWN).send_keys(Keys.ENTER)
    
    def fill_number_of_positions(self, number_of_position: int):
        self.wait.until(EC.presence_of_element_located(self.NUMBER_OF_POSITIONS_INPUT)).send_keys(number_of_position)
    
    def click_save_button(self):
        self.get_element(self.SAVE_BUTTON).click()
    
    # Perform complete actions   
    def perform_complete_add_vacancy(self, vacancy_name:str, job_title: str, description: str, number_of_position: int):
           self.click_add_button()
           self.fill_vacancy_name(vacancy_name)
           self.select_from_dropdown()
           self.select_job_tiltle(job_title)
           self.fill_description(description)
           self.fill_hiring_manager()
           self.fill_number_of_positions(number_of_position)
           self.click_save_button