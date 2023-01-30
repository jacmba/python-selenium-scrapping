from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.pluralsight.com")
driver.quit()

options = webdriver.FirefoxOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--headless")
driver = webdriver.Firefox(options = options)

driver.get("https://www.pluralsight.com")