import pytest
import allure
from src.PageObject.Pages.LoginRegister import LoginRegisterPage

page = LoginRegisterPage()


@pytest.fixture()
def initial_actions():
    page.openApp()
    yield
    page.logout()
    page.closeApp()


@allure.step
def test_realCredentials(initial_actions):
    # logging in with existing credentials ability verification
    email, password = "dexter@y.ru", "12345"
    page.login(email, password)
    # if "Logout" button is displayed on the Header, logging in is successfully done
    element = page.driver.find_element_by_link_text("Logout")
    assert element.is_displayed() is True