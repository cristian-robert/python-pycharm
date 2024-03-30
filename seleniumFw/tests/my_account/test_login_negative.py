import pytest
from seleniumFw.src.pages.MyAccountSignedOut import MyAccountSignedOut
from seleniumFw.src.helpers.faker_generator import FakerGenerator
@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid01
    def test_login_non_existing_user(self):
        my_account_page = MyAccountSignedOut(self.driver)
        faker = FakerGenerator()
        username = faker.generate_random_string(10)
        password = faker.generate_random_string(10)
        expected_error_message = f'Error: The username {username} is not registered on this site.' \
                                 ' If you are unsure of your username, try your email address instead.'


        my_account_page.go_to_my_account()
        # input non existing user with a random string of 15 characters
        my_account_page.input_login_username(username)
        my_account_page.input_login_password(password)
        my_account_page.click_login_button()
        my_account_page.check_error_message(expected_error_message)

