from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import time
#from PageObjects import 

class Test1:
    urlBase = "https://www.saucedemo.com/"
    urlInventory = "https://www.saucedemo.com/inventory.html" 
    username = "standard_user"
    password = "secret_sauce"
    
    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.urlBase)
        yield
        self.driver.quit()
        
        
    def test_login_com_falha(self, setup):
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        assert self.driver.current_url == self.urlBase, 'URL Obtida: ' + self.driver.current_url + ' URL Esperada: ' + self.urlBase
        assert self.driver.find_element(By.XPATH, "//h3[text()='Epic sadface: Username is required']"), 'Mensagem de erro não exibida'
    
    def test_login_com_sucesso(self, setup):        
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Username']").send_keys(self.username)
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']").send_keys(self.password)

        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        assert self.driver.current_url == self.urlInventory, 'URL Obtida: ' + self.driver.current_url + ' URL Esperada: ' + self.urlInventory
        #assert self.driver.find_element(By.XPATH, "//h3[text()='Epic sadface: Username is required']"), 'Mensagem de erro não exibida'
    
    def test_exibir_tela_produtos(self, setup):        
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Username']").send_keys(self.username)
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']").send_keys(self.password)

        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        
        assert self.driver.current_url == self.urlInventory, 'URL Obtida: ' + self.driver.current_url + ' URL Esperada: ' + self.urlInventory
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == 'Products'
        assert len(self.driver.find_elements(By.CSS_SELECTOR, ".inventory_list")) > 0
        assert len(self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item")) > 0
        
    def test_realizar_logout(self, setup):
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Username']").send_keys(self.username)
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']").send_keys(self.password)

        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        
        #assert login with success
        assert self.driver.find_element(By.CSS_SELECTOR, '.bm-burger-button').is_displayed()
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == 'Products'
        
        #logoff actions
        self.driver.find_element(By.CSS_SELECTOR, '.bm-burger-button').click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            EC.element_to_be_clickable(self.driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link'))
            )
        element.click()
        
        #assert logoff with success
        assert self.driver.current_url == self.urlBase
        
        
#por classe:
# .nomeClasse
#por id:
# #nomeId
#por atributo:
# attr [attr]
# attr=valor  [attr='valor']