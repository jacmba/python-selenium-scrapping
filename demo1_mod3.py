from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

ffOptions = Options()
ffOptions.add_argument("--kiosk")

driver = webdriver.Firefox(options=ffOptions)
driver.get("https://www.pluralsight.com")

time.sleep(3)
menu = driver.find_element_by_class_name("ps-nav-menu")
search = menu.find_element_by_class_name("ps-nav-search")
ele = search.find_element_by_tag_name("button")
ele.click()

time.sleep(1)
q = driver.find_element_by_name("q")
q.clear()
q.send_keys("Design patterns")
q.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()