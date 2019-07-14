from src.PageObject import Locators as l
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def jump_to_home_page():
    l.driver.find_element(*l.homeHeader).click()


def addTitle(title):
    l.driver.find_element(*l.noteTitle).send_keys(title)


def addContent(content):
    l.driver.find_element(*l.noteContent).send_keys(content)


def saveThis():
    l.driver.find_element(*l.saveButton).click()


def deleteNote():
    l.driver.find_element(*l.deleteButton).click()
    # waiting for the deleting confirmation alert being displayed. In case it isn't - report
    # this step is to help us see what caused the second verification failure if it did
    try:
        WebDriverWait(l.driver, 5).until(ec.alert_is_present())
        del_alert = l.driver.switch_to.alert
        del_alert.accept()
        print("-- delete confirmation alert accepted --")
    except:
        print("-- delete confirmation alert failed to display --")


def addNewNote():
    l.driver.find_element(*l.addNewNoteButton).click()


def createNote(title='Test Note', content='My Test Note Content'):
    jump_to_home_page()
    addTitle(title)
    addContent(content)
    saveThis()
    # wait till the note's title is displayed among the saved notes
    WebDriverWait(l.driver, 5).until(ec.visibility_of_element_located((By.LINK_TEXT, title)))
    return By.LINK_TEXT, title


def savedNotesBlockText():
    return l.driver.find_element(*l.savedNotesBlock).text


def alert_creating_notes_as_unregistered():
    return l.driver.find_element(*l.msg_creatingNotesAsUnregistered).text

