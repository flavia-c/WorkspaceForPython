from selenium.webdriver.common.by import By
from TestExample.Utils import Utils


class GmailHomePage:
    __INBOX_BUTTON = (By.XPATH, './/span/a[contains(text(), "Inbox")]')

    def __init__(self, driver):
        self.driver = driver
        Utils.wait_element_to_be_visible(self, self.driver, *GmailHomePage.__INBOX_BUTTON)

    def inbox_button_is_displayed(self):
        inbox_button = Utils.return_web_element(self, self.driver, *GmailHomePage.__INBOX_BUTTON)

        return inbox_button.is_displayed()