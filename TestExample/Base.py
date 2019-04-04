import pytest
from selenium import webdriver


class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.driver = webdriver.Chrome("C:\\Users\\flavia.croitoru\\Downloads\\chromedriver.exe")
        self.driver.get('http://accounts.google.com/')

        yield self.driver  # provide the fixture value

        print("Close Web Browser")
        self.driver.close()
        self.driver.quit()