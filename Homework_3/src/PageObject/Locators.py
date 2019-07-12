from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Locators(object):

    """
    contains basic web-driver operations functions, common to all pages operations,
    and locators of all buttons and fields of the http://anotepad.com web application
    """

    def __init__(self):
        # web driver by now. Gonna change an approach to reference it later
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def openApp(self):
        # opens anotepad web application
        self.driver.get("https://anotepad.com/")
        self.driver.maximize_window()

    def closeApp(self):
        # closes anotepad web application
        self.driver.quit()

    def newTab(self):
        # opens new tab in a browser (uses JavaScript)
        self.driver.execute_script("window.open('');")

    def closeTab(self):
        # closes a web-browser tab
        self.driver.close()

    def element_visibility(self, element):
        # verifies if the element given as an argument displayed on the screen
        # names of elements are given here as locators below
        try:
            return self.driver.find_element(*element).is_displayed()
        except:
            return False


################
#   LOCATORS   #
################

# Header
    homeHeader = (By.LINK_TEXT, 'Home')
    registerLoginHeader = (By.LINK_TEXT, 'Register/Login')
    logoutHeader = (By.LINK_TEXT, 'Logout')
    featuresHeader = (By.LINK_TEXT, 'Features')
    aboutHeader = (By.LINK_TEXT, 'About')
    settingsHeader = (By.LINK_TEXT, 'Settings')

# Home page locators
    noteTitle = (By.ID, 'edit_title')
    noteContent = (By.ID, 'edit_textarea')
    saveButton = (By.ID, 'btnSaveNote')
    addNewNoteButton = (By.LINK_TEXT, 'Add New Note')
    deleteButton = (By.CSS_SELECTOR, '.delete')
    savedNotesBlock = (By.CLASS_NAME, 'saved_notes')
    msg_creatingNotesAsUnregistered = (By.XPATH, '/html/body/div[2]/div/p[1]')

# Registration locators
    registrationEmail = (By. ID, 'registerEmail')
    registrationPassword = (By. CSS_SELECTOR, 'input[placeholder= "New Password"]')
    createAccountButton = (By. XPATH, '//button[contains(.,"Create Account")]')

# Login locators
    loginEmail = (By. ID, 'loginEmail')
    loginPassword = (By. CSS_SELECTOR, 'input[placeholder= "Enter Password"]')
    loginButton = (By. XPATH, '//button[contains(.,"Login")]')
    rememberMe = (By. CSS_SELECTOR, 'input[name="remember"]')
    forgotPassword = (By. LINK_TEXT, 'Forgot password?')

# Settings locators
    deleteAccountCheckbox = (By.CSS_SELECTOR, 'input[id="confirmDeleteAccount"]')
    deleteAccountButton = (By.CSS_SELECTOR, 'input[id="btnDeleteAccount"]')

