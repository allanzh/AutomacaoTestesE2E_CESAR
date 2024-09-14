from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.basePage import BasePage

class LoginPage(BasePage):
    #Variables
    url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    
    #Locators
    btn_submit = (By.XPATH, '//input[@type="submit"]')
    msg_error = (By.XPATH, "//h3[text()='Epic sadface: Username is required']")
    
    def __init__(self) -> None:
        super(LoginPage, self).__init__(None)
        
    
    def open_login(self):
        #self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        self.driver.get(self.url)
    
    def fill_login_fields(self, username=username, password=password):
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Username']").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']").send_keys(password)
        self.click_login_button()
        
    def click_login_button(self):
        #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.find_element(*self.btn_submit).click()

    def verify_url_login(self):
        return self.verify_url(self.url)
    
    def verify_error_message(self):
        return self.driver.find_element(*self.msg_error)
    
