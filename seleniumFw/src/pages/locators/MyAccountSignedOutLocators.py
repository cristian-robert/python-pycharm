from selenium.webdriver.common.by import By

class MyAccountSignedOutLocators:
    LOGIN_USER_NAME = (By.ID, 'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[value="Log in"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'ul.woocommerce-error')
    REGISTER_USERNAME = (By.ID, 'reg_username')
    REGISTER_PASSWORD = (By.ID, 'reg_password')
    REGISTER_EMAIL = (By.ID, 'reg_email')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[value="Register"]')

