import pytest

from TestExample.Base import Base
from TestExample.LoginAccountPage import LoginAccountPage


@pytest.mark.usefixtures('set_up')
class TestLogin(Base):

    __WRONG_ACCOUNT_ERROR = "Couldn't find your Google Account"
    __EMPTY_ACCOUNT_FIELD_ERROR = "Enter an email or phone number"
    __WRONG_PASSWORD_ERROR = "Wrong password. Try again or click Forgot password to reset it."

    def test_incorrect_account(self, set_up):
        login_page = LoginAccountPage(set_up)
        login_page.login_email_step('adss', False)

        assert TestLogin.__WRONG_ACCOUNT_ERROR == login_page.get_login_error_text()

    def test_empty_account(self, set_up):
        login_page = LoginAccountPage(set_up)
        login_page.login_email_step('', False)

        assert TestLogin.__EMPTY_ACCOUNT_FIELD_ERROR == login_page.get_login_error_text()

    def test_wrong_password(self, set_up):
        login_page = LoginAccountPage(set_up)
        password_page = login_page.login_email_step('testionut@gmail.com')
        password_page.login_password_step("blabla", False)

        assert TestLogin.__WRONG_PASSWORD_ERROR == password_page.get_password_error_text()

    # def test_login_correct_account(self, set_up):
    #     login_page = LoginAccountPage(set_up)
    #     password_page = login_page.login_email_step('Your Email adress')
    #     home_page = password_page.login_password_step("your password")
    #
    #     assert home_page.inbox_button_is_displayed() is True