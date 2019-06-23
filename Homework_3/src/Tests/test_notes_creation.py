import pytest
import allure
from src.PageObject.Pages.HomePage import HomePage

page = HomePage()


@pytest.fixture
def initial_actions():
    page.openApp()
    yield
    page.closeApp()


@allure.title('GL-242:F-15.2: Non-registered users. Creating notes ability verification')
def test_notes(initial_actions):
    page.addTitle('My new note')
    page.addContent('Some text')
    page.saveThis()

