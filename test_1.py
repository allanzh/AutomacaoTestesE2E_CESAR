from selenium import webdriver
from selenium.webdriver.common.by import By
from test_config import *
#from PIL import Image
from pages.loginPage import LoginPage

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
        
        # driver.save_screenshot("Login_Failed_Actual.png")
        # screenAtual = Image.open("Login_Failed_Actual.png")
        # screenEsperada = Image.open("Login_Failed_Expected.png")
        
        # assert screenEsperada == screenAtual
        
    def test_pageObjectModel_login_com_falha(self):
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        # driver.get(urlBase)
        loginPage = LoginPage()
        loginPage.open_login()
        
        #driver.find_element(By.XPATH, "//input[@type='submit']").click()
        loginPage.click_login_button()

        #assert driver.current_url == urlBase, 'URL Obtida: ' + driver.current_url + ' URL Esperada: ' + urlBase
        assert loginPage.verify_url_login(), 'URL obtida foi diferente da esperada'
        
        #assert driver.find_element(By.XPATH, "//h3[text()='Epic sadface: Username is required']"), 'Mensagem de erro não exibida'
        assert loginPage.verify_error_message() , 'Mensagem de erro não exibida'
        
        # driver.save_screenshot("Login_Failed_Actual.png")
        # screenAtual = Image.open("Login_Failed_Actual.png")
        # screenEsperada = Image.open("Login_Failed_Expected.png")
        
        # assert screenEsperada == screenAtual
#por classe:
# .nomeClasse
#por id:
# #nomeId
#por atributo:
# attr [attr]
# attr=valor  [attr='valor']