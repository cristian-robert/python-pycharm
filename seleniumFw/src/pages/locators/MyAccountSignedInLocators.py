from selenium.webdriver.common.by import By

class MyAccountSignedInLocators:
    # My Account
    LEFT_LOGOUT_NAV_BTN = (By.XPATH, "//li[@class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-"
                                     "navigation-link--customer-logout']//a[contains(text(),'Log out')]")
