import pytest
from selenium import webdriver
import os
from seleniumFw.src.helpers.config_helpers import get_base_url

@pytest.fixture(scope="class")
def init_driver(request):
    pass
    supported_browsers = ['chrome', 'headless-chrome', 'firefox']

    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported."
                        f"Supported are: {supported_browsers}")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        #options to not display popups
        options.add_argument("--disable-notifications")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        driver = webdriver.Chrome(options=options)
    driver.get(get_base_url())

    request.cls.driver = driver
    yield
    driver.quit()

    # driver = webdriver.
