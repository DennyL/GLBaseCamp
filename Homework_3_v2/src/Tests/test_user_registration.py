import pytest
import allure
from src.PageObject import Locators as l
from src.PageObject.Pages import LoginRegisterPage as lrp
from src.PageObject.Pages import SettingsPage as sp
from src.TestData import TestData as td


@pytest.fixture(scope="session")
def initial_actions():
    l.openApp()
    yield
    try:
        sp.deleteAccount()
        l.closeApp()
    except:
        l.closeApp()


@allure.title('GL-369:F-40: A free user account creation ability verification')
def test_registration(initial_actions):
    # new account creation ability verification
    lrp.create_an_account(td.test_logins[0], td.test_passwords[0])
    # if "Logout" button is displayed on the Header, logging in is successfully done
    assert l.element_visibility(l.logoutHeader) is True, 'Logout button was not displayed'
