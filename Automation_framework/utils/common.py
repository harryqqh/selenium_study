from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys


def enter(self, locator, text):
    """Enter text into a web element located by the given locator."""
    element = self.wait.until(EC.presence_of_element_located(locator))
    element.clear()
    element.send_keys(text)
