from selenium import webdriver
from selenium.webdriver.common.by import By

class ProductsPage:
    url = 'https://www.saucedemo.com/inventory.html'
    products_title = 'Products'
    
    #Locators
    element_page_title = (By.CSS_SELECTOR, ".title")
    element_inventory_list = (By.CSS_SELECTOR, ".inventory_list")
    element_inventory_item = (By.CSS_SELECTOR, ".inventory_item")
        
    def __init__(self, driver) -> None:
        self.driver = driver
        
    def verify_url_products_page(self):
        return self.driver.current_url == self.url
    
    def verify_page_title(self):
        return self.driver.find_element(*self.element_page_title).text == self.products_title
    
    
    def verify_has_inventory_list(self):
        return len(self.driver.find_elements(*self.element_inventory_list)) > 0
    
    def verify_has_inventory_items(self):
        return len(self.driver.find_elements(*self.element_inventory_item)) > 0
