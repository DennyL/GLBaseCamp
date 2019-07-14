from src.PageObject import Locators as l


def jump_to_settings_page():
    l.driver.find_element(*l.settingsHeader).click()


def deleteAccount():
    jump_to_settings_page()
    l.driver.find_element(*l.deleteAccountCheckbox).click()
    l.driver.find_element(*l.deleteAccountButton).click()
