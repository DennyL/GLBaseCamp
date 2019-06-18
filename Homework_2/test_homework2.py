import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(scope="session")
def environment_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://anotepad.com/')
    driver.maximize_window()  # just for better view
    yield
    driver.close()


def test_creating(environment_setup):

    """
    STEP 1: Open Google Chrome, then - the "anotepad.com" page.
    Create a note as a non-registered user, and
    verify presence of a corresponding message.
    """

    driver.find_element_by_id('edit_title').send_keys("My First Note")
    driver.find_element_by_id('btnSaveNote').click()
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/p[1]')))

    # verification that message_1 (on saving notes as a GuestUser) appeared
    with open('test_data/message1.txt') as expected_message1:
        assert driver.find_element_by_xpath("/html/body/div[2]/div/p[1]").text == expected_message1.read()


def test_delete(environment_setup):

    """
    STEP 2: Delete the note, and verify presence of "No notes here." in the page.
    """

    driver.find_element_by_class_name('delete').click()
    # waiting for the deleting confirmation alert to get displayed. In case it isn't - report
    # this step is to help us see what caused the second verification failure if it did
    try:
        WebDriverWait(driver, 5).until(ec.alert_is_present())
        del_alert = driver.switch_to.alert
        del_alert.accept()
        print("-- delete confirmation alert accepted --")
    except:
        print("-- delete confirmation alert failed to display --")

    # verification that message_2 ("No notes here") message appeared
    assert driver.find_element_by_class_name("saved_notes").text == 'No note here.'


