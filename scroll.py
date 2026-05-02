import time
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://demoapps.qspiders.com/ui/scroll')
driver.maximize_window()
driver.find_element('xpath','//a[text()="Open In New Tab"]').click()
wid=driver.window_handles
driver.switch_to.window(wid[1])

ob=ActionChains(driver)

ob.scroll_by_amount(500,0).perform()
ob.scroll_by_amount(-200,0).perform()
time.sleep(2)
