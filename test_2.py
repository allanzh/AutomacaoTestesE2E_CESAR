from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Conditions
from selenium.webdriver.common.by import By
from test_config import *
from pages.productsPage import ProductsPage
from pages.menuHamburgerPage import MenuHamburgerPage

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
        assert products.verify_page_title()
        assert products.verify_has_inventory_list()
        assert products.verify_has_inventory_items() 
        #len(driver.find_elements(By.CSS_SELECTOR, ".inventory_item")) > 0
        
    def test_realizar_logout_POM(self, setup, login):
        loginPage = login    
        products = ProductsPage(loginPage.driver)    
        menuPage = MenuHamburgerPage(loginPage.driver)
        
        products.verify_is_logged()
        menuPage.click_logoff()
        assert loginPage.verify_url_login()
        