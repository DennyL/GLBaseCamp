from src.PageObject import Locators as l


def jump_to_about_page():
    l.driver.find_element(*l.aboutHeader).click()
