import pytest

from seleniumFw.src.helpers.faker_generator import FakerGenerator
from seleniumFw.src.pages.MyAccountSignedIn import MyAccountSignedIn
from seleniumFw.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:
    @pytest.mark.tcid02
    def test_register_new_valid_user(self):
        my_account_signed_out_page = MyAccountSignedOut(self.driver)
        my_account_signed_in_page = MyAccountSignedIn(self.driver)
        faker = FakerGenerator()
        my_account_signed_out_page.go_to_my_account()
        my_account_signed_out_page.input_register_username(faker.username())
        my_account_signed_out_page.input_register_email(faker.email())
        my_account_signed_out_page.input_register_password(faker.generate_random_string(10))
        my_account_signed_out_page.click_register_button()
        assert my_account_signed_in_page.check_logout_button()
