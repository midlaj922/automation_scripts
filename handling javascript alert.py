import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(r'https://testautomationpractice.blogspot.com/')
driver.maximize_window()

# simple alert

driver.find_element("id","alertBtn").click()
time.sleep(3)
pop=driver.switch_to.alert
pop.accept()
time.sleep(3)

# confirmation alert

driver.find_element("id","confirmBtn").click()
time.sleep(3)
pop=driver.switch_to.alert
pop.accept()
# pop.dismiss()
time.sleep(3)

# prompt aler

driver.find_element("id","promptBtn").click()
time.sleep(3)
pop=driver.switch_to.alert
pop.send_keys('jhon wick')
pop.accept()
time.sleep(3)