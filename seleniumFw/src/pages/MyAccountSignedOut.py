from seleniumFw.src.pages.locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators
from seleniumFw.src.SeleniumExtended import SeleniumExtended
from seleniumFw.src.helpers.config_helpers import get_base_url
from selenium.webdriver.common.by import By

class MyAccountSignedOut(MyAccountSignedOutLocators):
    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_send_keys(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_send_keys(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    def check_error_message(self, text):
        return self.sl.wait_until_elements_contains_text(self.ERROR_MESSAGE, text)

    def input_register_username(self, username):
        self.sl.wait_and_send_keys(self.REGISTER_USERNAME, username)

    def input_register_password(self, password):
        self.sl.wait_and_send_keys(self.REGISTER_PASSWORD, password)

    def input_register_email(self, email):
        self.sl.wait_and_send_keys(self.REGISTER_EMAIL, email)

    def click_register_button(self):
        self.sl.wait_and_click(self.REGISTER_BUTTON)


