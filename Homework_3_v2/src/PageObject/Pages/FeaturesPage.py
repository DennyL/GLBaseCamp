from src.PageObject.Locators import Locators


class FeaturesPage(Locators):

    def jump_to_features_page(self):
        self.driver.find_element(*self.featuresHeader).click()
