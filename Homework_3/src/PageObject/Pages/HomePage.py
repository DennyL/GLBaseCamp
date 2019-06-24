from src.PageObject.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


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
        self.driver.find_element(*self.deleteButton).click()
        # waiting for the deleting confirmation alert being displayed. In case it isn't - report
        # this step is to help us see what caused the second verification failure if it did
        try:
            WebDriverWait(self.driver, 5).until(ec.alert_is_present())
            del_alert = self.driver.switch_to.alert
            del_alert.accept()
            print("-- delete confirmation alert accepted --")
        except:
            print("-- delete confirmation alert failed to display --")

    def addNewNote(self):
        self.driver.find_element(*self.addNewNoteButton).click()

    def createNote(self, title='Test Note', content='My Test Note Content'):
        self.jump_to_home_page()
        self.addTitle(title)
        self.addContent(content)
        self.saveThis()
        # wait till the note's title is displayed among the saved notes
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.LINK_TEXT, title)))
        return By.LINK_TEXT, title

    def savedNotesBlockText(self):
        return self.driver.find_element(*self.savedNotesBlock).text

    def alert_creating_notes_as_unregistered(self):
        return self.driver.find_element(*self.msg_creatingNotesAsUnregistered).text

