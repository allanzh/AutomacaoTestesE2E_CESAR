from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Conditions
from selenium.webdriver.common.by import By
from test_config import *
from pages.productsPage import ProductsPage

class Test2:

    def test_login_com_sucesso(self, setup, login):
        loginPage = login    
        products = ProductsPage(loginPage.driver)
        assert products.verify_page_title()
        assert products.verify_url_products_page()
        # driver.current_url == urlInventory, 'URL Obtida: ' + driver.current_url + ' URL Esperada: ' + urlInventory
        
    def test_exibir_tela_produtos(self, setup, login):  
        loginPage = login    
        products = ProductsPage(loginPage.driver)    
        assert products.verify_url_products_page()
        assert products.verify_url_products_page()
        assert products.verify_has_inventory_list()
        assert products.verify_has_inventory_items() 
        #len(driver.find_elements(By.CSS_SELECTOR, ".inventory_item")) > 0
        
    def test_realizar_logout(self, setup, login):
        driver = login
        #assert login with success
        assert driver.find_element(By.CSS_SELECTOR, '.bm-burger-button').is_displayed()
        assert driver.find_element(By.CSS_SELECTOR, ".title").text == 'Products'
        
        #logoff actions
        driver.find_element(By.CSS_SELECTOR, '.bm-burger-button').click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(
# passando elemento como uma tupla diretamente:
# Conditions.element_to_be_clickable(((By.CSS_SELECTOR, '#logout_sidebar_link')))
# a linha anterior substitui a necessidade do uso de self.driver.find_element :
# Conditions.element_to_be_clickable( self.driver.find_element (By.CSS_SELECTOR, '#logout_sidebar_link'))
            Conditions.element_to_be_clickable(((By.CSS_SELECTOR, '#logout_sidebar_link')))
            )
        element.click()
        
        #assert logoff with success
        assert driver.current_url == urlBase
        
