import pytest
import allure
from src.PageObject import Locators as l
from src.PageObject.Pages import LoginRegisterPage as lrp
from src.TestData import TestData as td


@pytest.fixture(scope="session")
def initial_actions():
    l.openApp()
    yield
    l.closeApp()


@allure.title('GL-497:F-180: Logging in with correct Email and Password')
def test_realCredentials(initial_actions):
    # logging in with existing credentials ability verification
    lrp.login(td.existing_test_login[0], td.existing_test_password[0])
    # if "Logout" button is displayed on the Header, logging in is successfully done
    assert l.element_visibility(l.logoutHeader) is True, 'Logout button was not displayed'
    lrp.logout()




