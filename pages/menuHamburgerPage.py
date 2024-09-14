from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Conditions

class MenuHamburgerPage:
    element_menu = (By.CSS_SELECTOR, '.bm-burger-button')
    element_btn_logout = (By.CSS_SELECTOR, '#logout_sidebar_link')
    
    def __init__(self, driver) -> None:
        self.driver = driver
    
    def menu_is_displayed(self):
        return self.driver.find_element(*self.element_menu).is_displayed()
    
    def open_menu(self):
        self.driver.find_element(*self.element_menu).click()
    
    def click_logoff(self):
        self.open_menu()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
        # passando elemento como uma tupla diretamente:
        # Conditions.element_to_be_clickable(((By.CSS_SELECTOR, '#logout_sidebar_link')))
        # a linha anterior substitui a necessidade do uso de self.driver.find_element :
        # Conditions.element_to_be_clickable( self.driver.find_element (By.CSS_SELECTOR, '#logout_sidebar_link'))
            Conditions.element_to_be_clickable(((self.element_btn_logout))))
        element.click()