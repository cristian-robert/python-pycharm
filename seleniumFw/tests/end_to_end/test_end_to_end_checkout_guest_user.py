import pytest
from faker import Faker

from seleniumFw.src.helpers.faker_generator import FakerGenerator
from seleniumFw.src.pages.CartPage import CartPage
from seleniumFw.src.pages.CheckoutPage import CheckoutPage
from seleniumFw.src.pages.Header import Header
from seleniumFw.src.pages.HomePage import HomePage
from seleniumFw.src.configs.generic_configs import GenericConfigs
@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid03
    def test_guest_user_can_checkout(self):
        home_page = HomePage(self.driver)
        header = Header(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        faker = Faker('en_GB')
        home_page.go_to_home_page()
        home_page.click_first_add_cart_button()

        header.wait_until_cart_item_count(1)
        header.click_right_cart_header()
        product_names = cart_page.get_all_product_names_in_cart()
        assert len(product_names) == 1, f'Expected 1 product in cart, but got {len(product_names)}'

        coupon_code = GenericConfigs.FREE_COUPON
        cart_page.apply_coupon('friends100')
        cart_page.click_proceed_to_checkout_button()

        checkout_page.input_email(faker.email())
        checkout_page.input_first_name(faker.first_name())
        checkout_page.input_last_name(faker.last_name())
        checkout_page.input_phone(faker.phone_number())
        checkout_page.input_address(faker.address())
        checkout_page.input_city(faker.city())
        checkout_page.input_postcode(faker.postcode())
        checkout_page.select_country(faker.country())
        checkout_page.select_county(faker.county())
        checkout_page.click_checkout_button()


