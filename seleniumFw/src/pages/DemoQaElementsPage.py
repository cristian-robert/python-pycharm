import pdb

from seleniumFw.src.helpers.faker_generator import FakerGenerator

from seleniumFw.src.SeleniumExtended import SeleniumExtended
from seleniumFw.src.pages.locators.DemoQaElementsLocators import DemoQaElementsLocators

class DemoQaElementsPage(DemoQaElementsLocators):

    generated_full_name = FakerGenerator().name()
    generated_email = FakerGenerator().email()
    generated_current_address = FakerGenerator().address()
    generated_permanent_address = FakerGenerator().address()

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def click_text_box(self):
        self.sl.wait_and_click(self.TEXT_BOX)

    def click_check_box(self):
        self.sl.wait_and_click(self.CHECK_BOX)

    def click_radio_button(self):
        self.sl.wait_and_click(self.RADIO_BUTTON)

    def click_web_tables(self):
        self.sl.wait_and_click(self.WEB_TABLES)

    def click_buttons(self):
        self.sl.wait_and_click(self.BUTTONS)

    def click_links(self):
        self.sl.wait_and_click(self.LINKS)



    #method to test text box
    def test_text_box(self):
        self.click_text_box()
        self.sl.wait_and_input_text(self.TEXT_BOX_FULL_NAME, self.generated_full_name)
        self.sl.wait_and_input_text(self.TEXT_BOX_EMAIL, self.generated_email)
        self.sl.wait_and_input_text(self.TEXT_BOX_CURRENT_ADDRESS, self.generated_current_address)
        self.sl.wait_and_input_text(self.TEXT_BOX_PERMANENT_ADDRESS, self.generated_permanent_address)
        self.sl.wait_scroll_and_click(self.TEXT_BOX_SUBMIT)
        self.sl.wait_until_element_contains_text(self.TEXT_BOX_NAME_RESULT, self.generated_full_name)
        self.sl.wait_until_element_contains_text(self.TEXT_BOX_EMAIL_RESULT, self.generated_email)
        self.sl.wait_until_element_contains_text(self.TEXT_BOX_CURRENT_ADDRESS_RESULT, self.generated_current_address)
        self.sl.wait_until_element_contains_text(self.TEXT_BOX_PERMANENT_ADDRESS_RESULT, self.generated_permanent_address)




