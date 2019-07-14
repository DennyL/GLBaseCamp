from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.PageObject import Locators as l


def jump_to_registerLogin_page():
    l.driver.find_element(*l.registerLoginHeader).click()


def login(email, password):
    jump_to_registerLogin_page()
    l.driver.find_element(*l.loginEmail).clear()
    l.driver.find_element(*l.loginPassword).clear()
    l.driver.find_element(*l.loginEmail).send_keys(email)
    l.driver.find_element(*l.loginPassword).send_keys(password)
    l.driver.find_element(*l.loginButton).click()


def logout():
    WebDriverWait(l.driver, 10).until(ec.visibility_of_element_located(l.logoutHeader))
    l.driver.find_element(*l.logoutHeader).click()


def create_an_account(email, password):
    jump_to_registerLogin_page()
    l.driver.find_element(*l.registrationEmail).send_keys(email)
    l.driver.find_element(*l.registrationPassword).send_keys(password)
    l.driver.find_element(*l.createAccountButton).click()

