import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.loginPage import LoginPage

urlBase = "https://www.saucedemo.com/"
urlInventory = "https://www.saucedemo.com/inventory.html" 
username = "standard_user"
password = "secret_sauce"

@pytest.fixture
def setup():
    loginPage = LoginPage()
    loginPage.open_login()
    yield loginPage
    loginPage.close()
    
#Fixture de login removida para a page de login    
@pytest.fixture
def login(setup):
    loginPage = setup
    loginPage.fill_login_fields()
    yield loginPage