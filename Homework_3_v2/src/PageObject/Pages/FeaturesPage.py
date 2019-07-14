from src.PageObject import Locators as l


def jump_to_features_page():
    l.driver.find_element(*l.featuresHeader).click()
