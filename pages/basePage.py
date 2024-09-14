from selenium import webdriver

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