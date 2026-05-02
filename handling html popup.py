import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://demoapps.qspiders.com/ui/hidden?sublist=0')
driver.maximize_window()


driver.find_element("xpath","//button[text()='Add Customer']").click()
driver.find_element("id","customerName").send_keys("Jhon Wick")
driver.find_element("id","customerEmail").send_keys("jhonwick@gmail.com")
drop=driver.find_element("id","prod")


obj=Select(drop)
a=obj.options

obj.select_by_value('Mobile')
time.sleep(2)
driver.find_element("id","message").send_keys("jhon wick need samsung ")
time.sleep(2)
driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(5)




time.sleep(3)