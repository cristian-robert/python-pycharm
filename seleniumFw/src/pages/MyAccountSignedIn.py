from seleniumFw.src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLocators
from seleniumFw.src.SeleniumExtended import SeleniumExtended
class MyAccountSignedIn(MyAccountSignedInLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def check_logout_button(self):
        return self.sl.check_element_displayed(self.LEFT_LOGOUT_NAV_BTN)