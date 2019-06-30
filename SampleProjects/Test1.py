from selenium import webdriver
import unittest
import HtmlTestRunner

#Trying to check if the newly configured git checks any kind of changes to this file

class YouTubeAutomation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome("C:/Users/Irfan/PycharmProjects/SeleniumTest/drivers/chromedriver.exe")
        cls.browser.maximize_window()

    def test_search_automation(self):
        self.browser.get("http://www.youtube.com")
        self.browser.find_element_by_id("search").send_keys("sexy dance")
        self.browser.find_element_by_id("search-icon-legacy").click()
        self.browser.find_element_by_id("video-title").click()

    # browser.find_element_by_class_name("gLFyf.gsfi").send_keys("how are you")
    # search_bar = browser.find_elements_by_name("q")

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output="C:/Users/Irfan/PycharmProjects/SeleniumTest/reports"))

