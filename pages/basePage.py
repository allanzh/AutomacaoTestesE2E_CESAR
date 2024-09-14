from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Conditions

class BasePage:
    
    def __init__(self, driver) -> None:
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            
    def verify_url(self, url):
        return self.driver.current_url == url
    
    def close(self):
        self.driver.close()
    
    def wait_element(self, element_tuple, timeout=5):
        return  WebDriverWait(self.driver, 10).until(
            Conditions.element_to_be_clickable(((element_tuple))))