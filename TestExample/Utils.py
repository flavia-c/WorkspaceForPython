from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Utils:

    @staticmethod
    def return_web_element(self, driver, *element_identifier):
        return driver.find_element(*element_identifier)

    @staticmethod
    def wait_element_to_be_visible(self, driver, *element_identifier, time_out=''):
        if time_out == '':
            time_out = 10

        # wait for element to be visible
        self.wait = WebDriverWait(driver, time_out)
        self.wait.until(ec.visibility_of_element_located(element_identifier))

    @staticmethod
    def return_element_text(self, driver, *element_identify) -> str:
        element = Utils.return_web_element(self, driver, *element_identify)
        text = element.text

        return text

    def return_first_class_or_second_class(driver, first_class, second_class, bool_condition =''):
        if bool_condition == '':
            bool_condition = True

        if bool_condition:
            return first_class(driver)
        else:
            return second_class(driver)