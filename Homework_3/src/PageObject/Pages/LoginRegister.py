from src.PageObject.Pages.SettingsPage import SettingsPage


class LoginRegisterPage(SettingsPage):

    def jump_to_registerLogin_page(self):
        self.driver.find_element(*self.registerLoginHeader).click()

    def login(self, email, password):
        self.jump_to_registerLogin_page()
        self.driver.find_element(*self.loginEmail).clear()
        self.driver.find_element(*self.loginPassword).clear()
        self.driver.find_element(*self.loginEmail).send_keys(email)
        self.driver.find_element(*self.loginPassword).send_keys(password)
        self.driver.find_element(*self.loginButton).click()

    def logout(self):
        self.driver.find_element(*self.logoutHeader).click()

    def create_an_account(self, email, password):
        self.jump_to_registerLogin_page()
        self.driver.find_element(*self.registrationEmail).send_keys(email)
        self.driver.find_element(*self.registrationPassword).send_keys(password)
        self.driver.find_element(*self.createAccountButton).click()

