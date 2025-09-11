import pytest
def test_hello_world():
    print("Hello World")
    

def verify_login_successful(self):
        #verify login successful by checking presence of profile element
        self.wait.until(EC.presence_of_element_located(self.profile))
        profile = self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
        assert profile.is_displayed()