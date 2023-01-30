from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

ffOptions = Options()
#ffOptions.add_argument("--kiosk")

driver = webdriver.Firefox(options=ffOptions)
driver.get("https://www.python.org")

ele = driver.find_element_by_id("id-search-field")
ele.send_keys("lists")
ele.send_keys(Keys.ENTER)

time.sleep(1)
ele_link = driver.find_element_by_link_text("Mailing Lists")
ele_link.click()

time.sleep(1)
ele_sublink = driver.find_element_by_partial_link_text("archive of python")
ele_sublink.click()

time.sleep(5)
#driver.quit()