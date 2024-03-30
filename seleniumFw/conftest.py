import allure
import pytest_html
from selenium import webdriver
import os
from seleniumFw.src.helpers.config_helpers import get_base_url
import logging
import sys

import pytest

from reportportal_client import RPLogger


@pytest.fixture(scope="function")
def init_driver(request):
    pass
    supported_browsers = ['chrome', 'headless-chrome', 'firefox']

    browser = os.environ.get('BROWSER', None)
    if not browser:
        browser = 'chrome'
        print(f"Browser not specified, defaulting to '{browser}'")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported."
                        f"Supported are: {supported_browsers}")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        # options to not display popups
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
    pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            if_frontend_test = True if 'init_driver' in item.fixturenames else False
            if if_frontend_test:
                results_dir = os.environ.get('RESULTS_DIR')
                print(f"results_dir: {results_dir}")
                if not results_dir:
                    results_dir = os.path.join(os.getcwd(), 'results')
                    print(f"results_dir not set, defaulting to: {results_dir}")
                screenshot_file = os.path.join(results_dir, item.name + ".png")
                driver = item.cls.driver
                try:
                    driver.save_screenshot(screenshot_file)
                except Exception as e:
                    print(f"Error occurred while saving screenshot: {str(e)}")
                extras.append(pytest_html.extras.image(screenshot_file))
        report.extras = extras


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            if_frontend_test = True if "init_driver" in item.fixturenames else False
            if if_frontend_test:
                results_dir = os.environ.get("RESULTS_DIR")
                if not results_dir:
                    results_dir = os.path.join(os.getcwd(), 'results')
                    print(f"results_dir not set, defaulting to: {results_dir}")
                screenshot_file = os.path.join(results_dir, item.name + ".png")
                driver = item.cls.driver
                try:
                    driver.save_screenshot(screenshot_file)
                    with open(screenshot_file, 'rb') as file:
                        allure.attach(file.read(), name="screenshot", attachment_type=allure.attachment_type.PNG)
                except Exception as e:
                    print(f"Error occurred while saving screenshot: {str(e)}")

    @pytest.fixture(scope="session")
    def rp_logger():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        logging.setLoggerClass(RPLogger)
        return logger
