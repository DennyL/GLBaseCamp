from src.PageObject.Locators import Locators


class LoginRegisterPage(Locators):

    def login(self, email, password):
        self.driver.find_element(*self.registerLoginHeader).click()
        self.driver.find_element(*self.loginEmail).send_keys(email)
        self.driver.find_element(*self.loginPassword).send_keys(password)
        self.driver.find_element(*self.loginButton).click()

    def logout(self):
        self.driver.find_element(*self.logoutHeader).click()

    def create_an_account(self, email, password):
        self.driver.find_element(*self.registerLoginHeader).click()
        self.driver.find_element(*self.registrationEmail).send_keys(email)
        self.driver.find_element(*self.registrationPassword).send_keys(password)
        self.driver.find_element(*self.createAccountButton).click()



