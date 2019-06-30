from selenium import webdriver
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from SampleProjects.pytest.Page.loginPage import LoginPage

# In pytest name of the module should start with 'test'#

class TestLogin(): # In pytest name of the class should start with 'test'
    driver = webdriver.Chrome("C:/Users/Irfan/PycharmProjects/SeleniumTest/drivers/chromedriver.exe")
    @pytest.fixture() # A test fixture represents the preparation needed to perform one or more tests, and any associate cleanup actions.
    def setup(self): # In pytest name of the setup is not required to start with 'test'
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()

    def test_login(self, setup): # In pytest name of the method should start with 'test'
        login = LoginPage(self.driver)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        #title = login.check_page_title()
        assert login.check_page_title() == "OrangeHRM"
