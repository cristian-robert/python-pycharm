from seleniumFw.src.SeleniumExtended import SeleniumExtended
from seleniumFw.src.enums.main_elements_paths import MainElementsPaths
from seleniumFw.src.pages.locators.DemoQaHomepageLocators import DemoQaHomepageLocators
from seleniumFw.src.helpers.config_helpers import get_base_url
from selenium.common.exceptions import NoSuchElementException

class DemoQaHomepage(DemoQaHomepageLocators):


    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def check_all_elements_displayed(self):
        for name, locator in vars(DemoQaHomepageLocators).items():
            # We're filtering out any non-locators (like built-in class methods)
            if isinstance(locator, tuple) and len(locator) == 2:
                if not self.driver.find_element(*locator).is_displayed():
                    print(f"{name} is not displayed!")
                    return False
        return True

    def click_element_and_check_link(self):
        for name, locator in vars(DemoQaHomepageLocators).items():
            if isinstance(locator, tuple) and len(locator) == 2:
                element = self.driver.find_element(*locator)
                element.location_once_scrolled_into_view
                element.click()

                expected_url = get_base_url() + MainElementsPaths[name].value
                assert self.driver.current_url == expected_url, f"URL mismatch for {name}"

                # Go back to the base URL
                self.driver.get(get_base_url())

    def go_to_elements_page(self):
        self.sl.wait_scroll_and_click(self.ELEMENTS_CARD)
        assert self.driver.current_url == get_base_url() + MainElementsPaths.ELEMENTS_CARD.value, "URL mismatch for Elements"


