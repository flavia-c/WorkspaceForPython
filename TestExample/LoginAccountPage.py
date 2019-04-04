from selenium.webdriver.common.by import By
from TestExample.LoginPasswordPage import LoginPasswordPage
from TestExample.Utils import Utils


class LoginAccountPage:
    __EMAIL_FIELD = (By.ID, 'identifierId')
    __NEXT_BUTTON = (By.ID, "identifierNext")
    __ERROR_LOGIN_ACCOUNT = (By.XPATH, ".//form[@method='post']/div[1]/div/div[2]/div[2]")

    def __init__(self, driver):
        self.driver = driver
        Utils.wait_element_to_be_visible(self, self.driver, *LoginAccountPage.__EMAIL_FIELD)

    def __set_email(self, email):
        email_field = Utils.return_web_element(self, self.driver, *LoginAccountPage.__EMAIL_FIELD)
        email_field.send_keys(email)

    def __click_submit(self):
        submit_button = Utils.return_web_element(self, self.driver, *LoginAccountPage.__NEXT_BUTTON)
        submit_button.click()

    def login_email_step(self, email, correct_email=''):
        self.__set_email(email)
        self.__click_submit()

        return Utils.return_first_class_or_second_class(self.driver, LoginPasswordPage, LoginAccountPage, correct_email)

    def get_login_error_text(self):
        Utils.wait_element_to_be_visible(self, self.driver, *LoginAccountPage.__ERROR_LOGIN_ACCOUNT)

        return Utils.return_element_text(self, self.driver, *LoginAccountPage.__ERROR_LOGIN_ACCOUNT)