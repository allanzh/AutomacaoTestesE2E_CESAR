from selenium import webdriver
from selenium.webdriver.common.by import By
from test_config import *

class Test1:
    # urlBase = "https://www.saucedemo.com/"
    # urlInventory = "https://www.saucedemo.com/inventory.html" 
    # username = "standard_user"
    # password = "secret_sauce"
        
    def test_login_com_falha(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(urlBase)
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        assert driver.current_url == urlBase, 'URL Obtida: ' + driver.current_url + ' URL Esperada: ' + urlBase
        assert driver.find_element(By.XPATH, "//h3[text()='Epic sadface: Username is required']"), 'Mensagem de erro não exibida'
    
#por classe:
# .nomeClasse
#por id:
# #nomeId
#por atributo:
# attr [attr]
# attr=valor  [attr='valor']