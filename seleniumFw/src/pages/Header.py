from seleniumFw.src.pages.locators.HeaderLocators import HeaderLocators
from seleniumFw.src.SeleniumExtended import SeleniumExtended


class Header(HeaderLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def click_right_cart_header(self):
        self.sl.wait_scroll_and_click(self.CART_HEADER_RIGHT)

    def wait_until_cart_item_count(self, count):
        if count > 1:
            expected_text = str(count) + ' items'
        else:
            expected_text = str(count) + ' item'

        self.sl.wait_until_element_contains_text(self.CART_ITEM_COUNT, expected_text)
