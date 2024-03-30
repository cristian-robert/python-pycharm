from selenium.common import TimeoutException, StaleElementReferenceException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        for _ in range(timeout):
            try:
                element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
                element.click()
                break
            except (StaleElementReferenceException, ElementNotVisibleException):
                pass
        else:
            raise Exception(f"Could not click the element at {locator} within {timeout} seconds")

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def wait_until_elements_contains_text(self, elements_locator, text, timeout=None):
        WebDriverWait(self.driver, timeout or self.default_timeout).until(
            lambda _: text in ''.join([element.text for element in self.driver.find_elements(*elements_locator)])
        )

    # wait and scroll to element and click method
    def wait_scroll_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def check_element_displayed(self, locator, timeout=None):
        timeout = timeout if timeout is not None else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def check_elements_displayed(self, *locators, timeout=None):
        results = {}
        for locator in locators:
            results[locator] = self.check_element_displayed(locator, timeout=timeout)
        return results

    def wait_and_send_keys(self, locator, keys, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(keys)

    def get_concatenated_text_from_elements(self, selector):
        return ''.join(element.text for element in self.driver.find_elements(By.CSS_SELECTOR, 'ul.woocommerce-error'))

    def wait_and_get_elements(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = err if err else f"Unable to find elements located by '{locator}'," \
                              f" after timeout of {timeout}."
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(err)
