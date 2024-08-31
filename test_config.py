import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

urlBase = "https://www.saucedemo.com/"
urlInventory = "https://www.saucedemo.com/inventory.html" 
username = "standard_user"
password = "secret_sauce"

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(urlBase)
    yield driver
    driver.quit()
    
@pytest.fixture
def login(setup):
    driver = setup
    driver.find_element(By.CSS_SELECTOR, "[placeholder='Username']").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    yield driver