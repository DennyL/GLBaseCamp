import pytest
import allure
from src.PageObject.Pages.HomePage import HomePage

page = HomePage()


@pytest.fixture()
def initial_actions():
    page.openApp()
    page.createNote()
    yield
    page.closeApp()


@allure.title('GL-244:F-15.4: Deleting notes ability verification')
def test_delete(initial_actions):
    page.deleteNote()
    assert page.savedNotesBlockText() == 'No note here.'
