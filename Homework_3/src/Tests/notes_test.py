import pytest
from src.PageObject.Pages.HomePage import HomePage

page = HomePage()


@pytest.fixture()
def initial_actions():
    page.openApp()
    yield
    page.closeApp()


def test_notes(initial_actions):
    page.addTitle('My new note')
    page.addContent('Some text')
    page.saveThis()







