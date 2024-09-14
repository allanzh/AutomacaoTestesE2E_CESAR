from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    url = "https://www.saucedemo.com/"
    btn_submit = (By.XPATH, '//input[@type="submit"]')
    msg_error = By.XPATH, "//h3[text()='Epic sadface: Username is required']"
    
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    
    def open_login(self):
        #self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        self.driver.get(self.url)
        
    def click_login_button(self):
        #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.find_element(*self.btn_submit).click()

    def verify_url_login(self):
        return self.driver.current_url == self.url#, 'URL Obtida: ' + self.driver.current_url + ' URL Esperada: ' + self.url
    
    def verify_error_message(self):
        return self.driver.find_element(*self.msg_error)#, 'Mensagem de erro não exibida'
    