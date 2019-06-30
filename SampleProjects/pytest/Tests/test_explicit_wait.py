from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome("C:/Users/Irfan/PycharmProjects/SeleniumTest/drivers/chromedriver.exe")

browser.get("https://www.expedia.com")

browser.implicitly_wait(5) # Implicit Wait

browser.find_element_by_id("tab-flight-tab-hp").click()

time.sleep(5)


origin = "SFO"
destination = "NYC"

origin_airport = browser.find_element_by_id("flight-origin-hp-flight")
origin_airport.clear()
for ele in origin:
    time.sleep(1)
    origin_airport.send_keys(ele)

time.sleep(5)

destination_airport = browser.find_element_by_id("flight-destination-hp-flight")
destination_airport.clear()
for ele in destination:
    time.sleep(1)
    destination_airport.send_keys(ele)

#.send_keys("NYC")
browser.find_element_by_id("flight-departing-hp-flight").send_keys("12/12/2019")
browser.find_element_by_id("flight-returning-hp-flight").send_keys("12/01/2020")
browser.find_element_by_xpath("//div[@class='ab25184-traveler-wrapper-flight available-for-flights gcw-clear-both']//button[@class='trigger-utility menu-trigger btn-utility btn-secondary dropdown-toggle theme-standard pin-left menu-arrow gcw-component gcw-traveler-amount-select gcw-component-initialized']").click()
browser.find_element_by_xpath("//div[@class='traveler-selector-sinlge-room-data traveler-selector-room-data']//div[@class='children-wrapper']//div[@class='uitk-grid step-input-outside gcw-component gcw-component-step-input gcw-step-input gcw-component-initialized']//button[@class='uitk-step-input-button uitk-step-input-plus']").click()
element = browser.find_element_by_id("flight-age-select-1-hp-flight")
# Drop down using Select class
drp_down = Select(element)
drp_down.select_by_value("4") # select by value from dropdown
#drp_down.select_by_index(3) # select by index from dropdown
values = drp_down.options
print(values)

browser.find_element_by_xpath("//form[@id='gcw-flights-form-hp-flight']//button[@class='btn-primary btn-action gcw-submit']").click()

wait=WebDriverWait(browser,10) # Explicit wait
stop = wait.until(EC.element_to_be_clickable((By.ID,"stopFilter_stops-0")))
stop.click()

browser.close()
browser.quit()