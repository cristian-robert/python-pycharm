from selenium.webdriver.common.by import By

class CheckoutPageLocators:
    EMAIL_INPUT = (By.ID, 'email')
    FIRST_NAME_INPUT = (By.ID, 'billing-first_name')
    LAST_NAME_INPUT = (By.ID, 'billing-last_name')
    PHONE_INPUT = (By.ID, 'billing-phone')
    ADDRESS_INPUT = (By.ID, 'billing-address_1')
    CITY_INPUT = (By.ID, 'billing-city')
    POSTCODE_INPUT = (By.ID, 'billing-postcode')
    COUNTRY_SELECT = (By.ID, 'components-form-token-input-0')
    COUNTY_SELECT = (By.ID, 'components-form-token-input-1')
    CREATE_ACCOUNT_CHECKBOX = (By.ID, 'control-checkbox-0')
    CHECKOUT_BUTTON = (By.CLASS_NAME, 'wc-block-components-checkout-place-order-button')
