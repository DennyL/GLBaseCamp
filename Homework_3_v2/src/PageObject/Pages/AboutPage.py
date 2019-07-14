from src.PageObject.Locators import Locators


class AboutPage(Locators):

    def jump_to_about_page(self):
        self.driver.find_element(*self.aboutHeader).click()
