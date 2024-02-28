from selenium.webdriver.common.by import By

class DemoQaHomepageLocators:
    ELEMENTS_CARD = (By.XPATH, "//h5[normalize-space()='Elements']")
    FORMS_CARD = (By.XPATH, "//h5[normalize-space()='Forms']")
    ALERTS_FRAMEWORKS_CARD = (By.XPATH, "//h5[normalize-space()='Alerts, Frame & Windows']")
    WIDGETS_CARD = (By.XPATH, "//h5[normalize-space()='Widgets']")
    INTERACTIONS_CARD = (By.XPATH, "//h5[normalize-space()='Interactions']")
    BOOK_STORE_APPLICATION_CARD = (By.XPATH, "//h5[normalize-space()='Book Store Application']")