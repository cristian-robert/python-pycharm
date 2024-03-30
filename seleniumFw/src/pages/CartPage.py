import time

from seleniumFw.src.pages.locators.CartPageLocators import CartPageLocators
from seleniumFw.src.SeleniumExtended import SeleniumExtended
import time

class CartPage(CartPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def get_all_product_names_in_cart(self):
        product_name_elements = self.sl.wait_and_get_elements(self.CART_PRODUCT_NAMES)
        product_names = [element.text for element in product_name_elements]
        return product_names

    def click_add_coupon_button(self):
        self.sl.wait_and_click(self.ADD_COUPON_BUTTON)

    def input_coupon_code(self, coupon_code):
        self.sl.wait_and_input_text(self.COUPON_CODE_INPUT, coupon_code)

    def click_apply_coupon_button(self):
        self.sl.wait_and_click(self.APPLY_COUPON_BUTTON)

    def check_coupon_applied(self, coupon_code):
        self.sl.wait_until_elements_contains_text(self.APPLIED_COUPON_TEXT, coupon_code)

    def apply_coupon(self, coupon_code):
        self.click_add_coupon_button()
        self.input_coupon_code(coupon_code)
        self.click_apply_coupon_button()
        self.check_coupon_applied(coupon_code)

    def click_free_shipping_radio(self):
        self.sl.wait_and_click(self.FREE_SHIPPING_RADIO)

    def click_proceed_to_checkout_button(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BUTTON, 5)

    def wait_for_selected_shipping_applied(self, text):
        self.sl.wait_until_element_contains_text(self.SHIPPING_VIA, text)