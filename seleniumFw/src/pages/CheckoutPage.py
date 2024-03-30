from seleniumFw.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators
from seleniumFw.src.SeleniumExtended import SeleniumExtended
from selenium.webdriver.common.keys import Keys

class CheckoutPage(CheckoutPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_email(self, email):
        self.sl.wait_and_input_text(self.EMAIL_INPUT, email)

    def input_first_name(self, first_name):
        self.sl.wait_and_input_text(self.FIRST_NAME_INPUT, first_name)

    def input_last_name(self, last_name):
        self.sl.wait_and_input_text(self.LAST_NAME_INPUT, last_name)

    def input_phone(self, phone):
        self.sl.wait_and_input_text(self.PHONE_INPUT, phone)

    def input_address(self, address):
        self.sl.wait_and_input_text(self.ADDRESS_INPUT, address)

    def input_city(self, city):
        self.sl.wait_and_input_text(self.CITY_INPUT, city)

    def input_postcode(self, postcode):
        self.sl.wait_and_input_text(self.POSTCODE_INPUT, postcode)

    def select_country(self, country):
        self.sl.wait_and_click(self.COUNTRY_SELECT)
        self.sl.wait_and_input_text(self.COUNTRY_SELECT, country)

    def select_county(self, county):
        self.sl.wait_and_click(self.COUNTY_SELECT)
        self.sl.wait_and_input_text(self.COUNTY_SELECT, county)

    def click_create_account_checkbox(self):
        self.sl.wait_and_click(self.CREATE_ACCOUNT_CHECKBOX)

    def click_checkout_button(self):
        self.sl.wait_and_click(self.CHECKOUT_BUTTON)