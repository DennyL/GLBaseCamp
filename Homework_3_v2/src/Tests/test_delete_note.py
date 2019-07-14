import pytest
import allure
from src.PageObject import Locators as l
from src.PageObject.Pages import HomePage as hp


@pytest.fixture(scope="session")
def initial_actions():
    l.openApp()
    hp.createNote()
    yield
    l.closeApp()


@allure.title('GL-244:F-15.4: Deleting notes ability verification')
def test_delete(initial_actions):
    hp.deleteNote()
    assert hp.savedNotesBlockText() == 'No note here.'
