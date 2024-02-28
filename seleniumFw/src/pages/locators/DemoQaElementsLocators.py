from selenium.webdriver.common.by import By


class DemoQaElementsLocators:
    # Text Box
    TEXT_BOX = (By.XPATH, "//span[text()='Text Box']")
    TEXT_BOX_FULL_NAME = (By.XPATH, "//input[@id='userName']")
    TEXT_BOX_EMAIL = (By.XPATH, "//input[@id='userEmail']")
    TEXT_BOX_CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    TEXT_BOX_PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")
    TEXT_BOX_SUBMIT = (By.XPATH, "//button[@id='submit']")
    TEXT_BOX_NAME_RESULT = (By.XPATH, "//p[@id='name']")
    TEXT_BOX_EMAIL_RESULT = (By.XPATH, "//p[@id='email']")
    TEXT_BOX_CURRENT_ADDRESS_RESULT = (By.XPATH, "//p[@id='currentAddress']")
    TEXT_BOX_PERMANENT_ADDRESS_RESULT = (By.XPATH, "//p[@id='permanentAddress']")

    # Check Box
    CHECK_BOX = (By.XPATH, "//span[text()='Check Box']")
    CHECK_BOX_HOME = (By.XPATH, "//span[text()='Home']")
    CHECK_BOX_DESKTOP = (By.XPATH, "//span[text()='Desktop']")
    CHECK_BOX_NOTES = (By.XPATH, "//span[text()='Notes']")
    CHECK_BOX_RESULT = (By.XPATH, "//span[@class='text-success']")

    # Radio Button
    RADIO_BUTTON = (By.XPATH, "//span[text()='Radio Button']")
    RADIO_BUTTON_YES = (By.XPATH, "//label[@for='yesRadio']")
    RADIO_BUTTON_IMPRESSIVE = (By.XPATH, "//label[@for='impressiveRadio']")
    RADIO_BUTTON_NO = (By.XPATH, "//label[@for='noRadio']")
    RADIO_BUTTON_RESULT_RADIO = (By.XPATH, "//span[@class='text-success']")

    # Web Tables
    WEB_TABLES = (By.XPATH, "//span[text()='Web Tables']")
    WEB_TABLES_ADD = (By.XPATH, "//button[@id='addNewRecordButton']")
    WEB_TABLES_FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    WEB_TABLES_LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    WEB_TABLES_EMAIL = (By.XPATH, "//input[@id='userEmail']")
    WEB_TABLES_AGE = (By.XPATH, "//input[@id='age']")
    WEB_TABLES_SALARY = (By.XPATH, "//input[@id='salary']")
    WEB_TABLES_DEPARTMENT = (By.XPATH, "//input[@id='department']")
    WEB_TABLES_SUBMIT = (By.XPATH, "//button[@id='submit']")
    WEB_TABLES_SEARCH = (By.XPATH, "//input[@id='searchBox']")
    WEB_TABLES_EDIT = (By.XPATH, "//button[@id='edit-record)")
    WEB_TABLES_DELETE = (By.XPATH, "//button[@id='delete-record-1']")
    WEB_TABLES_RESULT = (By.XPATH, "//div[@class='rt-tr -odd']//div[@class='rt-td'][1]")
    WEB_TABLES_RESULT_SEARCH = (By.XPATH, "//div[@class='rt-tr -odd']//div[@class='rt-td'][1]")
    WEB_TABLES_RESULT_EDIT = (By.XPATH, "//div[@class='rt-tr -odd']//div[@class='rt-td'][1]")
    WEB_TABLES_RESULT_DELETE = (By.XPATH, "//div[@class='rt-tr -odd']//div[@class='rt-td'][1]")
    WEB_TABLES_RESULT_SEARCH_EMPTY = (By.XPATH, "//div[@class='rt-tr -odd']//div[@class='rt-td'][1]")

    # Buttons
    BUTTONS = (By.XPATH, "//span[text()='Buttons']")
    DOUBLE_CLICK = (By.XPATH, "//button[@id='doubleClickBtn']")
    RIGHT_CLICK = (By.XPATH, "//button[@id='rightClickBtn']")
    CLICK_ME = (By.XPATH, "//button[@id='doubleClickBtn']")
    RESULT_DOUBLE_CLICK = (By.XPATH, "//p[@id='doubleClickMessage']")
    RESULT_RIGHT_CLICK = (By.XPATH, "//p[@id='rightClickMessage']")
    RESULT_CLICK_ME = (By.XPATH, "//button[@id='doubleClickBtn']")

    # Links
    LINKS = (By.XPATH, "//span[text()='Links']")
    HOME = (By.XPATH, "//a[text()='Home']")
    CREATED = (By.XPATH, "//a[text()='Created']")
    NO_CONTENT = (By.XPATH, "//a[text()='No Content']")
    MOVED = (By.XPATH, "//a[text()='Moved']")
    BAD_REQUEST = (By.XPATH, "//a[text()='Bad Request']")
    UNAUTHORIZED = (By.XPATH, "//a[text()='Unauthorized']")
    FORBIDDEN = (By.XPATH, "//a[text()='Forbidden']")
    NOT_FOUND = (By.XPATH, "//a[text()='Not Found']")
    INTERNAL_SERVER_ERROR = (By.XPATH, "//a[text()='Internal Server Error']")
    RESULT_HOME = (By.XPATH, "//h1[text()='Home']")
    RESULT_CREATED = (By.XPATH, "//h1[text()='Created']")
    RESULT_NO_CONTENT = (By.XPATH, "//h1[text()='No Content']")

