from selenium.webdriver.common.by import By


class CartPageLocators:
    CART_PRODUCT_NAMES = (By.CSS_SELECTOR, '.wc-block-components-product-name')
    ADD_COUPON_BUTTON = (By.CLASS_NAME, 'wc-block-components-totals-coupon-link')
    COUPON_CODE_INPUT = (By.ID, 'wc-block-components-totals-coupon__input-0')
    APPLY_COUPON_BUTTON = (By.CLASS_NAME, 'wc-block-components-totals-coupon__button')
    APPLIED_COUPON_TEXT = (By.CSS_SELECTOR, 'li .screen-reader-text')
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'a.wc-block-cart__submit-button')
    FREE_SHIPPING_RADIO = (By.ID, "input[id*='free_shipping']")
    SHIPPING_VIA = (By.CLASS_NAME, 'wc-block-components-totals-shipping__via')

