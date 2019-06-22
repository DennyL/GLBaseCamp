import pytest
import allure
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


@allure.title('GL-369:F-40: A free user account creation ability verification')
def test_registration(initial_actions):
    # new account creation ability verification
    page.create_an_account('raw@ya.net', '12345')
    # if "Logout" button is displayed on the Header, logging in is successfully done
    assert page.element_visibility(page.logoutHeader) is True, 'Logout button was not displayed'

