from selenium.webdriver.common.by import By

from TestExample.GmailHomePage import GmailHomePage
from TestExample.Utils import Utils


class LoginPasswordPage:
    __PASSWORD_FIELD = (By.NAME, 'password')
    __NEXT_BUTTON = (By.ID, "passwordNext")
    __ERROR_PASSWORD_ACCOUNT = (By.XPATH, ".//*[@id='password']/div[2]/div[2]")

    def __init__(self, driver):
        self.driver = driver
        Utils.wait_element_to_be_visible(self, self.driver, *LoginPasswordPage.__PASSWORD_FIELD)

    def __set_password(self, password):
        password_field = Utils.return_web_element(self, self.driver, *LoginPasswordPage.__PASSWORD_FIELD)
        password_field.send_keys(password)

    def __click_submit(self):
        submit_button = Utils.return_web_element(self, self.driver, *LoginPasswordPage.__NEXT_BUTTON)
        submit_button.click()

    def login_password_step(self, password, correct_password=''):
        self.__set_password(password)
        self.__click_submit()

        return Utils.return_first_class_or_second_class(self.driver, GmailHomePage, LoginPasswordPage, correct_password)

    def get_password_error_text(self):
        Utils.wait_element_to_be_visible(self, self.driver, *LoginPasswordPage.__ERROR_PASSWORD_ACCOUNT)

        return Utils.return_element_text(self, self.driver, *LoginPasswordPage.__ERROR_PASSWORD_ACCOUNT)