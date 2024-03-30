from seleniumFw.src.SeleniumExtended import SeleniumExtended
from seleniumFw.src.pages.locators.HomePageLocators import HomePageLocators
from seleniumFw.src.helpers.config_helpers import get_base_url

class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        home_page_url = get_base_url()
        self.driver.get(home_page_url)

    def click_first_add_cart_button(self):
        self.sl.wait_scroll_and_click(self.ADD_CART_BUTTON)