from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from SampleProjects.POMProject.Pages.loginPage import LoginPage
from SampleProjects.POMProject.Pages.homePage import HomePage
from webdriver_manager.chrome import ChromeDriverManager


class LoginTest(unittest.TestCase): # A testcase is subclassed from unittest.TestCase

    @classmethod
    def setUpClass(cls): # class setup method executed only once at the beginning of the class
        #cls.driver = webdriver.Chrome("C:/Users/Irfan/PycharmProjects/SeleniumTest/drivers/chromedriver.exe")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_valid_login(self): # name of the test method in unittest should start with 'test'
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        homepage = HomePage(self.driver)
        homepage.click_welcome()
        homepage.select_logout()

    def test_02_invalid_login(self): # name of the test method in unittest should start with 'test'
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin12")
        login.click_login()
        login.not_login()
        message = login.not_login()
        self.assertEquals(message, "Invalid credentials")


    @classmethod
    def tearDownClass(cls): # clas teardown method executed only once at the end of the class
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__': # this is used so that test can be executed/run from command line
        unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output= "C:/Users/Irfan/PycharmProjects/SeleniumTest/reports"))

