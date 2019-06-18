import pytest
from src.PageObject.Pages.LoginRegister import LoginRegisterPage

page = LoginRegisterPage()


@pytest.fixture()
def initial_actions():
    page.openApp()
    yield
    try:
        page.logout()
    except:
        page.closeApp()


def test_registration(initial_actions):
    # new account creation ability verification
    page.create_an_account('raw@ya.net', '12345')
    # if "Logout" button is displayed on the Header, logging in is fulfilled
    element = page.driver.find_element_by_link_text("Logout")
    assert element.is_displayed() is True

