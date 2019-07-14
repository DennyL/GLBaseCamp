import pytest
import allure
from src.PageObject import Locators as l
from src.PageObject.Pages import HomePage as hp


@pytest.fixture(scope="session")
def initial_actions():
    l.openApp()
    yield
    l.closeApp()


@allure.title('GL-242:F-15.2: Non-registered users. Creating notes ability verification')
def test_notes_creation_nr(initial_actions):
    # new_note variable contains the locator of the note after it was saved
    new_note = hp.createNote()
    # verification that alert of creating notes as the non-registered user is displayed
    assert hp.alert_creating_notes_as_unregistered() == "You have saved your note as a Guest User. You can come back at anytime to continue editing as long as you don't delete your browser cookies. To access your notes from anywhere and never lose them, please Create a Free Account. Your existing notes will be saved into your account."
    # now, verification that the note title is displayed among the saved notes. For this we use new_note variable
    assert l.element_visibility(new_note) is True
