from src.PageObject.Locators import Locators


class HomePage(Locators):

    def jump_to_home_page(self):
        self.driver.find_element(*self.homeHeader).click()

    def addTitle(self, title):
        self.driver.find_element(*self.noteTitle).send_keys(title)

    def addContent(self, content):
        self.driver.find_element(*self.noteContent).send_keys(content)

    def saveThis(self):
        self.driver.find_element(*self.saveButton).click()

    def deleteNote(self):
        pass

    def addNewNote(self):
        self.driver.find_element(*self.addNewNoteButton).click()





