from selenium import webdriver

browser = webdriver.Chrome("C:/Users/Irfan/PycharmProjects/SeleniumTest/drivers/chromedriver.exe")

browser.get("http://newtours.demoaut.com")

browser.implicitly_wait(10)

assert "Welcome: Mercury Tours" in browser.title

browser.find_element_by_css_selector("input[type=text]").send_keys("mercury")
browser.find_element_by_css_selector("input[type=password").send_keys("mercury")
browser.find_element_by_css_selector("input[value=Login]").click()

browser.close()
browser.quit()