from src.PageObject.Locators import Locators


class SettingsPage(Locators):

    def jump_to_settings_page(self):
        self.driver.find_element(*self.settingsHeader).click()

    def deleteAccount(self):
        self.jump_to_settings_page()
        self.driver.find_element(*self.deleteAccountCheckbox).click()
        self.driver.find_element(*self.deleteAccountButton).click()
